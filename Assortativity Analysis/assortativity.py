import pandas as pd
import numpy as np
import networkx as nx

G = nx.read_graphml("MACN.graphml")

for node, data in G.nodes(data=True):
    data['Citation.Count'] = int(data['Citation.Count']/100)

field_assortativity = nx.attribute_assortativity_coefficient(G,'Field.of.Interest')
print("Field of Interest:", field_assortativity)

h_index_assortativity = nx.numeric_assortativity_coefficient(G,'h.index')
print("h-index:", h_index_assortativity)

country_assortativity = nx.attribute_assortativity_coefficient(G,'Country')
print("Country:", country_assortativity)

institute_assortativity = nx.attribute_assortativity_coefficient(G,'Institute.ID')
print("Institute:", institute_assortativity)

citation_count_assortativity = nx.numeric_assortativity_coefficient(G,'Citation.Count')
print("Citation Count:", citation_count_assortativity)

gender_assortativity = nx.attribute_assortativity_coefficient(G,'Gender')
print("Gender:", gender_assortativity)

degree_assortativity = nx.degree_assortativity_coefficient(G)
print("Node Degree:", degree_assortativity)
