# cycle_number_ranking_method

A cost-effective approach to identify multiple influential spreaders based on cycle structure in networks

1、Background

Node importance ranking is a very hot research field in complex network, and the existing methods, including degree centrality, K-core, H-index, etc., are calculated by chain or star structure, few scholars take into account the cycle structure in the network. Therefore, this project starts from a special kind of cycles in the network - basic cycles. By calculating the number of basic cycles of nodes, the nodes in the network are sorted according to the number of basic cycles, and the feasibility of this method is verified through network propagation. At the same time, this project can also calculate the cost of network propagation nodes. By calculating the cost and comparing the propagation ability, we can screen out more ideal propagation seeds, and also provide a method to verify the superiority of the algorithm for other node importance ranking algorithms.
  
2、Experimental tools and methods

（1）Data: we conduct experiments on six real networks, which are undirected and unweighted. C. elegans is a neural network of the Caenorhabditis elegans nematode, with nodes representing neurons and links representing synapses or gap junctions among two neurons. USA airports is a flight network among all commercial airports in the United States. The original network is directed, we simply transfer it into undirected in the analysis. Its nodes represent airports and a link between two nodes indicates that there exists an airline between the two airports. Yeast is a protein-protein interactions network in budding yeast. Soc-hamsterster is a friendship network from the Hamsterster website in which nodes represent users and links denote friend or family relationships. Asian-last.fm is a social network of Last.FM users, which was collected from the public API in March 2020. This network describes the mutual follower relationships between users from Asian countries. Router is a communication network, where nodes represent autonomous systems and a link connecting two nodes indicates that the two systems have traffic exchange.

（2）Benchmarks:

We consider six common-used indicators with different mechanisms and a newly proposed cycle-based metric as benchmark indicators:

Degree centrality (DC), Coreness (KC), Collective influence (CI), H-index (HI), Closeness centrality (CC), Eigenvector centrality (EC), Cycle ratio (CR).

（3）Network spreading model: SIR model。

3、File introduction

（1）data: The data folder contains all the experimental data required for the project, including the txt data of six networks ('Soc-hamsterster','Router','USAairports','Yeast ','Lastfm_asia', 'C. elegans'). The six networks cover biological, routing, airline, social and other network types, with the number of nodes ranging from 200 to 7600.

（2）creat_network_by_txt.py: Run this file, the txt file in the data folder can be used to generate the network graph required by the project;

（3）H-index_methods.py, collective_influence_methods.py: These two files implement the H-index (HI) and Collective influence (CI) algorithms respectively. By running these two files, you can generate the node ranking of HI and CI；

（4）cycle_number_methoods.py: This file implements the node ranking algorithm by using the number of basic cycles (NC) in the network；

（5）metheds_rank.py: This file realizes the node ranking of all other comparison algorithms except HI and CI, and unifies the results of all algorithms into the same file according to the node ID, which is convenient for subsequent network propagation experiments；

（6）kendall.py: This file is used to calculate the kendall correlation of the node ranking of each indicator in the six networks；

（7）SIR_model.py: This file implements the SIR disease transmission model；

（8）score_SIR.py: This file uses metheds_rank.py filters out the top-N nodes, and then uses SIR_model.py conducts multi-source propagation experiments on the SIR model. The top-N nodes and the number of experiments can be customized；

（9）cost.py: This file is used to calculate the cost of node filtering. By comprehensively considering the cost and propagation ability, a more ideal set of propagation seeds can be selected.
