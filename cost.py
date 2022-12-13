
import networkx as nx
import numpy as np
'''
程序主要功能：
计算传播源的筛选代价
'''
def cost(graph,top_k_nodes):
    degree_list = nx.degree_histogram(graph)
    degree = list(nx.degree(graph, top_k_nodes))
    sum_cost = 0
    for i in range(len(degree)):
        cost = degree[i][1] / (degree_list[degree[i][1]] / np.sum(degree_list))
        sum_cost += cost
    return sum_cost
