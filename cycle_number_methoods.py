
import networkx as nx
import json
def NC_method(G):
    # 计算图G的所有基本圈
    list_cycle_basis = nx.cycle_basis(G)
    # 根据基本圈集合，计算出网络中每个节点所拥有的基本圈数量
    nodes_cycle_num = {}
    for list_cycle in list_cycle_basis:
        for i in list_cycle:
            if i not in nodes_cycle_num:
                nodes_cycle_num[i] = 1
            elif i in nodes_cycle_num:
                nodes_cycle_num[i] += 1
    # 返回圈数字典
    return nodes_cycle_num
if __name__ == '__main__':
    # 数据
    NetWorks = ['Soc-hamsterster', 'Router','USA airports','Yeast','Lastfm_asia','Celegans']
    for network in NetWorks:
        print('Reading {} gpickle'.format(network))
        G = nx.read_gpickle('./data/{}/{}.gpickle'.format(network, network))
        with open('./data/{}/{}-nodes_cycle_num.json'.format(network, network), 'w', encoding='UTF-8') as fp:
            fp.write(json.dumps(NC_method(G), indent=2, ensure_ascii=False))