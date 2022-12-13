import networkx as nx
'''
程序主要功能：
从txt文件创建图文件
'''
NetWorks = ['Soc-hamsterster', 'Router','USA airports','Yeast','Lastfm_asia','Celegans']
for network in NetWorks:
    # 加载边数据
    print('')
    print('Reading {} edgelist'.format(network))
    network_edges_dir = './data/{}/{}.txt'.format(network,network)
    with open(network_edges_dir, 'rb')as edges_f:
        network_g = nx.read_edgelist(edges_f, nodetype=int, create_using=nx.Graph(), encoding='latin1',
                                     data=(('weight', float),))
    nx.write_gpickle(network_g,'./data/{}/{}.gpickle'.format(network,network)) # 存储图形对象
