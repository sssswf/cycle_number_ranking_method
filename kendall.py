import networkx as nx
import numpy as np
import pandas as pd
import json
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.stats import kendalltau
if __name__ == '__main__':
    NetWorks = ['Soc-hamsterster', 'Router','USA airports','Yeast','Lastfm_asia','Celegans']
    corr_matrix= np.zeros((8, 8))
    for network in NetWorks:
        print('Reading {} gpickle'.format(network))
        graph = nx.read_gpickle('./data/{}/{}.gpickle'.format(network, network))
        metheds = pd.read_csv('./data/{}/{}_methods_rank.csv'.format(network, network))  # 多种方法(a,b,c,d)的排序结果
        methods_name = np.array(metheds.columns)[1: len(metheds.columns)]
        pd.set_option("max_columns", 1000)
        df1 = metheds[
            ['EC',  'CC','DC','NC','CI','KC','HI',]]
        cc_corr = df1.corr(method='kendall')  # 相关系数矩阵
        corr_matrix = corr_matrix + cc_corr
    mpl.rcParams['font.sans-serif'] = 'Times New Roman'
    print(corr_matrix / 6)
    plt.subplots(figsize=(9, 6), dpi=300, facecolor='w')  # 设置画布大小，分辨率，和底色
    cmap = sns.diverging_palette(200, 20, sep=16, as_cmap=True)
    fig = sns.heatmap(corr_matrix / 6, annot=True, vmax=1, square=True, cmap=cmap, fmt='.2g')
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.savefig('./graph/df_corr.svg',bbox_inches='tight',transparent=False)#保存图片
    plt.show()
