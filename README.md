# cycle_number_ranking_method

从圈结构的视角研究复杂网络中的节点重要性排序

一、项目背景

节点重要性排序是当前复杂网络中十分火热的研究领域，而现存的方法，包括度中心性、K-core、H-index等都是通过链式或者星型结构来进行计算的，很少有人考虑到网络中的圈结构。因此，本项目从网络中的一类特殊圈——基本圈出发，通过计算节点的基本圈的数量，对网络中的节点按照基本圈数量的大小进行排序，并通过网络传播验证该方法的可行性。同时，本项目还能计算网络传播节点的代价，通过计算代价并对比传播能力，可以筛选出更理想的传播种子，同时也为其他节点重要性排序算法提供了一个验证算法优越性的方法。
  
二、实验工具和方法概述

1、实验数据：6个网络数据集；

2、实验对比算法：

Degree centrality (DC)、Coreness (KC)、Collective influence (CI)、H-index (HI)、Closeness centrality (CC)、Eigenvector centrality (EC)、Cycle ratio (CR)；

3、实验模型：SIR疾病传播模型。

三、项目文件介绍

1、data文件夹：data文件夹中放置了本项目所需要的所有实验数据，共包含6个网络的txt文本数据（'Soc-hamsterster', 'Router','USA airports','Yeast','Lastfm_asia','Celegans'），6个网络分别涵盖生物、路由、航空、社交等网络类型，节点数量从200到7600不等；

2、creat_network_by_txt.py：该文件运行后可以利用data文件夹中的txt文件生成后续项目所需要的网络图；

3、H-index_methods.py、collective_influence_methods.py：这两个文件分别实现了H-index (HI)和Collective influence (CI)算法，通过运行这两个文件，可以生成HI和CI的节点排序；

4、cycle_number_methoods.py：该文件实现了利用网络中的基本圈圈数进行节点排序的算法；

5、metheds_rank.py：该文件实现了除HI、CI的其他所有对比算法的节点排序，并且将所有算法的结果按照节点ID统一到了同一个文件中，方便后续网络传播实验；

6、kendall.py：该文件用于计算各个指标在6个网络中计算出的节点排序的相关性；

7、SIR_model.py：该文件实现了SIR疾病传播模型；

8、score_SIR.py：该文件通过利用metheds_rank.py将多个指标的前N个节点筛选出来，然后利用SIR_model.py进行SIR模型上的多源传播实验，其中前N个节点可以自定义，实验次数也可以自定义；

9、cost.py：该文件用于计算节点筛选时所耗费的代价，通过综合考虑代价和传播能力，可以选出更理想的传播种子。
