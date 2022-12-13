import networkx as nx
import numpy as np
import pandas as pd
import json
'''
程序主要功能：
计算多个网络的多个指标，并把它们按照节点ID放在同一个文件夹
'''
NetWorks = ['Soc-hamsterster', 'Router','USA airports','Yeast','Lastfm_asia','Celegans']
for network in NetWorks:
    print('Reading {} gpickle'.format(network))
    G = nx.read_gpickle('./data/{}/{}.gpickle'.format(network, network))
    #EC方法
    with open('./data/{}/{}-nodes_EC.json'.format(network, network), 'w', encoding='UTF-8') as fp:
        fp.write(json.dumps(nx.eigenvector_centrality(G), indent=2, ensure_ascii=False))
    with open('./data/{}/{}-nodes_EC.json'.format(network, network), 'r', encoding='UTF-8') as f:
        EC = json.load(f)
    EC_list = []
    for i, v in EC.items():
        EC_list.append([int(i), v])
    # DC方法
    degree_cen_dict = nx.degree_centrality(G)
    degree_cen_list = []
    for key,value in degree_cen_dict.items():
        degree_cen_list.append([key,value])
    # CC方法
    closeness_cen_dict = nx.closeness_centrality(G)
    closeness_cen_list = []
    for key,value in closeness_cen_dict.items():
        closeness_cen_list.append([key,value])
    # NC方法
    with open('./data/{}/{}-nodes_cycle_num.json'.format(network, network), "r") as f:
        cycle_dict_0 = json.load(f)
    cycle_list_0 = []
    for i,v in cycle_dict_0.items():
        cycle_list_0.append([int(i),v])
    # KC方法
    with open('./data/{}/{}-nodes_k_core_num.json'.format(network, network), 'w', encoding='UTF-8') as fp:
        fp.write(json.dumps(nx.core_number(G), indent=2, ensure_ascii=False))
    with open('./data/{}/{}-nodes_k_core_num.json'.format(network, network), "r") as f:
        core = json.load(f)
    core_list = []
    for i,v in core.items():
        core_list.append([int(i),v])
    # CI方法
    with open('./data/{}/{}-nodes_CI_new.json'.format(network, network), 'r', encoding='UTF-8') as f:
        CI = json.load(f)
    CI_list = []
    for i, v in CI.items():
        CI_list.append([int(i), v])
    # HI方法
    with open('./data/{}/{}-h_index.json'.format(network, network), 'r', encoding='UTF-8') as f:
        HI_fake = json.load(f)
    HI_fake_list = []
    for i, v in HI_fake.items():
        HI_fake_list.append([int(i), v])
    with open('./data/{}/{}-h_index.json'.format(network, network), 'r', encoding='UTF-8') as f:
        HI = json.load(f)
    HI_list = []
    for i, v in HI.items():
        HI_list.append([int(i), v])

    # 将产生的多个文件汇总成一个文件
    df1 = pd.DataFrame(EC_list,columns=['node_ID','EC'])
    df2 = pd.DataFrame(degree_cen_list, columns=['node_ID','DC'])
    df3 = pd.DataFrame(closeness_cen_list, columns=['node_ID','CC'])
    df1_2 = pd.merge(df1, df2, on='node_ID')
    df1_3 = pd.merge(df1_2, df3, on='node_ID')
    df4 = pd.DataFrame(cycle_list_0, columns=['node_ID','NC'])
    df1_4 = pd.merge(df1_3,df4,on='node_ID',how="left").fillna(0)
    df5 = pd.DataFrame(core_list, columns=['node_ID', 'KC'])
    df1_5 = pd.merge(df1_4, df5, on='node_ID', how="left").fillna(0)
    df6 = pd.DataFrame(CI_list, columns=['node_ID', 'CI'])
    df1_6 = pd.merge(df1_5, df6, on='node_ID', how="left").fillna(0)
    df7 = pd.DataFrame(HI_list, columns=['node_ID', 'HI'])
    df = pd.merge(df1_6, df7, on='node_ID', how="left").fillna(0)
    df.to_csv("data/{}/{}_methods_rank.csv".format(network, network),index=None)
    print('{}保存成功'.format(network))