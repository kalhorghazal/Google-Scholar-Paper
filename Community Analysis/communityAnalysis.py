!pip install python-igraph

import igraph as ig
import networkx as nx
import pandas as pd
import os.path as path
import numpy as np
import networkx.algorithms.community as nx_comm

G = nx.read_graphml("MACN.graphml")
G.remove_nodes_from(list(nx.isolates(G)))

nx.write_graphml(G,'graph.graphml')
g = ig.read('graph.graphml',format="graphml")

mapping = {}
for v in g.vs:
    mapping[g.vs[v.index]['id']] = v.index

H = nx.relabel_nodes(G, mapping)

communities = pd.DataFrame(columns=['Community Size', 'Mean Citation Count', 'Mean h-index'])

for c in g.community_infomap():
    community =  H.subgraph(c)
    
    h_index = nx.get_node_attributes(community,'h.index')
    mean_h_index = np.array([h_index[k] for k in h_index]).mean()
    
    citation_count = nx.get_node_attributes(community,'Citation.Count')
    mean_citation_count = np.array([citation_count[k] for k in citation_count]).mean()
    
    communities.loc[len(communities.index)] = [len(c), mean_citation_count, mean_h_index]

communities.to_csv('communities_data.csv', index=False)
