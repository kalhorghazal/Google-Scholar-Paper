import pandas as pd
import numpy as np
import networkx as nx

G = nx.read_graphml("FIN.graphml")

mylist = list(G.degree(weight='weight'))

mylist.sort(key=lambda x: x[1], reverse=True)
mylist[0:20]

pagerank = nx.pagerank(G, weight="weight")
sorted(pagerank.items(), key=lambda item: item[1], reverse=True)[0:20]

betweenness = nx.betweenness_centrality(G)
sorted(betweenness.items(), key=lambda item: item[1], reverse=True)

closeness = nx.closeness_centrality(G)
sorted(closeness.items(), key=lambda item: item[1], reverse=True)[0:40]

eigenvector = nx.eigenvector_centrality(G, weight="weight")
sorted(eigenvector.items(), key=lambda item: item[1], reverse=True)[0:20]
