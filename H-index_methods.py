import networkx as nx
import json
def my_Hindex(Mygraph):
    HindexDict = dict()
    # print("list(Mygraph.nodes())  ", len(list(Mygraph.nodes())), list(Mygraph.nodes()))
    for curnode in list(Mygraph.nodes()):  # 全部节点
        # print(" curnode = %d  邻居数：" % (curnode),Mygraph.degree(curnode))
        if Mygraph.degree(curnode) == 0:
            HindexDict[curnode] = 0
            continue
        neighborList = [[0 for col in range(2)] for row in range(Mygraph.degree(curnode))]
        index = 0
        for j in Mygraph.neighbors(curnode):
            neighborList[index][0] = j  # 邻居的索引
            neighborList[index][1] = Mygraph.degree(j)  # 邻居的度
            index += 1
        neighborList.sort(key=lambda d: d[1], reverse=True)
        for i in range(Mygraph.degree(curnode)):
            hin = i+1
            if i+1 < len(neighborList):
                if neighborList[i][1] >= hin and neighborList[i+1][1] < hin+1:
                    HindexDict[curnode] = hin
                    break
            else:
                HindexDict[curnode] = hin
    return HindexDict
if __name__ == '__main__':
    # 数据
    NetWorks = ['Soc-hamsterster', 'Router','USA airports','Yeast','Lastfm_asia','Celegans']
    for network in NetWorks:
        print('Reading {} gpickle'.format(network))
        graph = nx.read_gpickle('./data/{}/{}.gpickle'.format(network, network))
        with open('./data/{}/{}-h_index.json'.format(network, network), 'w', encoding='UTF-8') as fp:
            fp.write(json.dumps(my_Hindex(graph), indent=2, ensure_ascii=False))

