import networkx as nx
import json
def Collective_Influence(G, l=2):
    Collective_Influence_Dic = {}
    node_set = G.nodes()
    for nid in node_set:
        CI = 0
        neighbor_set = []
        neighbor_hop_1 = list(G.neighbors(nid))
        neighbor_hop_2 = []
        for nnid in neighbor_hop_1:
            neighbor_hop_2  = list(set(neighbor_hop_2).union(set(G.neighbors(nnid))))
        # print("{}:{}".format(nid, neighbor_hop_1))
        # print("{}:{}".format(nid,neighbor_hop_2))

        center = [nid]
        neighbor_set = list(   set(neighbor_hop_2).difference(   set(neighbor_hop_1).union(set(center))  )    )
        # print("{}:{}".format(nid, neighbor_set))
        total_reduced_degree = 0
        for id in neighbor_set:
            total_reduced_degree = total_reduced_degree + (G.degree(id)-1.0)
        #end
        # print("{}:{}".format(nid, total_reduced_degree))
        CI = (G.degree(nid)-1.0) * total_reduced_degree
        Collective_Influence_Dic[nid] = CI
    #end for
    #print "Collective_Influence_Dic:",sorted(Collective_Influence_Dic.iteritems(), key=lambda d:d[1], reverse = True)
    return Collective_Influence_Dic

if __name__ == '__main__':
    # 数据
    NetWorks = ['Soc-hamsterster', 'Router','USA airports','Yeast','Lastfm_asia','Celegans']
    for network in NetWorks:
        print('Reading {} gpickle'.format(network))
        G = nx.read_gpickle('./data/{}/{}.gpickle'.format(network, network))
        with open('./data/{}/{}-nodes_CI_new.json'.format(network, network), 'w', encoding='UTF-8') as fp:
            fp.write(json.dumps(Collective_Influence(G), indent=2, ensure_ascii=False))