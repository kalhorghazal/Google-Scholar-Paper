!pip install python-igraph

import igraph as ig
import networkx as nx
import os.path as path
import numpy as np
import pandas as pd

fields = pd.read_csv("users_fields.csv")
G = nx.read_graphml("directed.graphml")

G.add_nodes_from(fields['user_id'].tolist())
node_attr = fields.set_index('user_id').to_dict('index')
nx.set_node_attributes(G, node_attr)

nx.write_graphml(G,'graph.graphml')
g = ig.read('graph.graphml',format="graphml")

mapping = {}
for v in g.vs:
    mapping[g.vs[v.index]['id']] = v.index

H = nx.relabel_nodes(G, mapping)

inv_map = {v: k for k, v in mapping.items()}

from collections import Counter

communities = pd.DataFrame(columns=['community_size', 'common_field', 'nodes'])

for c in g.community_infomap():
    community =  H.subgraph(c)
    nodes = [inv_map[i] for i in list(community.nodes)]  
    if (len(c) <= 1):
      continue
    attr = nx.get_node_attributes(community,'field')
    attr_list = list(attr.values())
    data = Counter(attr_list)
    get_mode = dict(data)
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
    if (len(mode) > 0):
      communities.loc[len(communities.index)] = [len(c), mode[0], nodes]

communities.to_csv('common_fields.csv', index=False)