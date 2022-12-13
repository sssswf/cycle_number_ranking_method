import random
import networkx as nx
import numpy as np
import pandas as pd
import csv
import time
from SIR_model import SIR_network
def getTopK(methods, k):
    # 循环每一个方法,找到top—k节点
    source_all = []
    for i in range(len(methods_name)):
        nodes_ID = methods.iloc[:, 0]
        method = methods.iloc[:, i + 1]  # 方法列
        index_top_K = method.argsort()[::-1][0:k]
        source = []
        for j in index_top_K:
            source.append(nodes_ID[j])
        source_all.append(source)
    return source_all
def infected_beta(graph):
    # SIR模型的感染率设置
    degree = nx.degree(graph)
    degree_list = []
    degree_sq_list = []
    for i in degree:
        degree_list.append(i[1])
        degree_sq_list.append(i[1] * i[1])
    degree_avg = np.mean(degree_list)
    degree_avg_sq = np.mean(degree_sq_list)
    infected = degree_avg / (degree_avg_sq -  2 *degree_avg)
    return infected
if __name__ == '__main__':
    # 数据
    NetWorks = ['Soc-hamsterster']
    for network in NetWorks:
        print('Reading {} gpickle'.format(network))
        graph = nx.read_gpickle('./data/{}/{}.gpickle'.format(network, network))
        metheds = pd.read_csv('./data/{}/{}_methods_rank.csv'.format(network, network))  # 多种方法(a,b,c,d)的排序结果
        methods_name = np.array(metheds.columns)[1: len(metheds.columns)]
        '''
        初始化存储每次SIR传播范围的csv文件
        设置top多少节点作为传播源
        '''
        for top_k in [20,50,100]:
            name = '2β'
            file = open('result/{}/{}_Top-'.format(network, network) + str(top_k) + ' SIR_{}.csv'.format(name), "w", newline="")
            content = csv.writer(file)
            content.writerow(['EC','DC','CC','CN','K-shell','CI','HI'])  # 写入文件列标题（各方法的名称）
            file.close()
            print('{}_Top-'.format(network) + str(top_k) + ' SIR_{}.csv 已初始化！'.format(name))
            file1 = open('result/{}/{}_Top-'.format(network, network) + str(top_k) + ' F_SIR_{}.csv'.format(name), "w", newline="")
            content1 = csv.writer(file1)
            content1.writerow(
                ['EC','DC','CC','CN','K-shell','CI','HI'])  # 写入文件列标题（各方法的名称）
            file1.close()
            print('{}_Top-'.format(network) + str(top_k) + ' F_SIR_{}.csv 已初始化！'.format(name))

            '''
            进行n次实验取平均值
            '''
        n = 1000
        for i in range(n):
            if i % 200 ==0:
                print('第 ' + str(i + 1) + ' 次实验')
            for top_k in [20,50,100]:
                source_all = getTopK(metheds, top_k)  # 多种方法的Top-k节点
                # SIR参数设置
                gamma = 0.5  # 免疫率
                beta = 2 *infected_beta(graph) * gamma # 感染率
                step = 40  # 迭代次数
                # top-k序列
                source_a = source_all[0]
                source_b = source_all[1]
                source_c = source_all[2]
                source_d = source_all[3]
                source_e = source_all[4]
                source_f = source_all[5]
                source_h = source_all[7]

                # Top-k节点的感染情况
                sir_a = SIR_network(graph, source_a, beta, gamma, step)
                sir_b = SIR_network(graph, source_b, beta, gamma, step)
                sir_c = SIR_network(graph, source_c, beta, gamma, step)
                sir_d = SIR_network(graph, source_d, beta, gamma, step)
                sir_e = SIR_network(graph, source_e, beta, gamma, step)
                sir_f = SIR_network(graph, source_f, beta, gamma, step)
                sir_h = SIR_network(graph, source_h, beta, gamma, step)
                # 存储每次实验的最终感染情况
                file = open('result/{}/{}_Top-'.format(network, network) + str(top_k) + ' SIR_{}.csv'.format(name))
                reader = csv.reader(file)
                original = list(reader)
                file1 = open('result/{}/{}_Top-'.format(network, network) + str(top_k) + ' SIR_{}.csv'.format(name), "w", newline="")
                content = csv.writer(file1)
                # 存储文件中的原始数据
                for row in original:
                    content.writerow(row)
                # 存储新数据
                content.writerow([sir_a[step - 1],sir_b[step - 1],sir_c[step - 1],sir_d[step - 1],sir_e[step - 1],sir_f[step - 1],
                                  sir_h[step - 1],
                                  ])
                file.close()
                file1.close()

                # 存储每次实验的传播效率
                sir_a_set = sorted(list(set(sir_a)))
                sir_b_set = sorted(list(set(sir_b)))
                sir_c_set = sorted(list(set(sir_c)))
                sir_d_set = sorted(list(set(sir_d)))
                sir_e_set = sorted(list(set(sir_e)))
                sir_f_set = sorted(list(set(sir_f)))
                sir_h_set = sorted(list(set(sir_h)))
                if sir_a_set[-1] - sir_a_set[0] != 0:
                    f_a = (sir_a_set[-1] - sir_a_set[0]) / (len(sir_a_set) - 1)
                else:
                    f_a = 0
                if sir_b_set[-1] - sir_b_set[0] != 0:
                    f_b = (sir_b_set[-1] - sir_b_set[0]) / (len(sir_b_set) - 1)
                else:
                    f_b = 0
                if sir_c_set[-1] - sir_c_set[0] != 0:
                    f_c = (sir_c_set[-1] - sir_c_set[0]) / (len(sir_c_set) - 1)
                else:
                    f_c = 0
                if sir_d_set[-1] - sir_d_set[0] != 0:
                    f_d = (sir_d_set[-1] - sir_d_set[0]) / (len(sir_d_set) - 1)
                else:
                    f_d = 0
                if sir_e_set[-1] - sir_e_set[0] != 0:
                    f_e = (sir_e_set[-1] - sir_e_set[0]) / (len(sir_e_set) - 1)
                else:
                    f_e = 0
                if sir_f_set[-1] - sir_f_set[0] != 0:
                    f_f = (sir_f_set[-1] - sir_f_set[0]) / (len(sir_f_set) - 1)
                else:
                    f_f = 0
                if sir_h_set[-1] - sir_h_set[0] != 0:
                    f_h = (sir_h_set[-1] - sir_h_set[0]) / (len(sir_h_set) - 1)
                else:
                    f_h = 0

                file2 = open('result/{}/{}_Top-'.format(network, network) + str(top_k) + ' F_SIR_{}.csv'.format(name))
                reader1 = csv.reader(file2)
                original1 = list(reader1)
                file3 = open('result/{}/{}_Top-'.format(network, network) + str(top_k) + ' F_SIR_{}.csv'.format(name), "w", newline="")
                content1 = csv.writer(file3)
                # 存储文件中的原始数据
                for row in original1:
                    content1.writerow(row)
                # 存储新数据
                content1.writerow([f_a,f_b,f_c,f_d,f_e,f_f,f_h])
                file2.close()
                file3.close()

        '''
        输出n次实验的平均值
        '''
        for top_k in [20,50,100]:
            sir_results = pd.read_csv('result/{}/{}_Top-'.format(network, network) + str(top_k) + ' SIR_{}.csv'.format(name))  # 多种方法的排序结果
            print('{}_Top-'.format(network) + str(top_k) + ' SIR(Average)')
            print(sir_results.describe(include='all').iloc[1])  # 输出数据特征
            print("-------------------------")
            sir_results1 = pd.read_csv(
                'result/{}/{}_Top-'.format(network, network) + str(top_k) + ' F_SIR_{}.csv'.format(name))  # 多种方法的排序结果
            print('{}_Top-'.format(network) + str(top_k) + ' F_SIR(Average)')
            print(sir_results1.describe(include='all').iloc[1])  # 输出数据特征
            print("########################")