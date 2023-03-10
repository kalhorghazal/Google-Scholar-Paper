import pandas as pd
import numpy as np
import networkx as nx
from random import choice

G = nx.read_graphml("MACN.graphml")

reciprocity = nx.reciprocity(G)
print("Reciprocity:", reciprocity)

G.remove_nodes_from(list(nx.isolates(G)))
H = G.to_undirected()
max_lcc = max(nx.connected_components(H), key=len)
max_wcc = H.subgraph(max_lcc)

clustering_coefficient = nx.average_clustering(max_wcc)
print("Clustering Coefficient:", clustering_coefficient)

total = 0
for i in range(1000):
  a = choice(list(max_wcc.nodes()))
  b = choice(list(max_wcc.nodes()))
  dist = nx.shortest_path_length(max_wcc, source=a, target=b, method='dijkstra')
  total += dist
average_shortest_path_length = total / 1000
print("Average Shortest Path Length:", average_shortest_path_length)
