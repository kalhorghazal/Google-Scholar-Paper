import pandas as pd
import numpy as np
import networkx as nx

G = nx.read_graphml("MACN.graphml")

H = G.to_undirected()

nodes = (
    node
    for node, data
    in G.nodes(data=True)
    if data.get("field") == "Computer Science"
)
computerSubgraph = H.subgraph(nodes)

computerRichClubCoefs = nx.rich_club_coefficient(computerSubgraph,normalized=True, Q=10, seed=131)

nodes = (
    node
    for node, data
    in G.nodes(data=True)
    if data.get("field") == "Physics and Astronomy"
)
physicsSubgraph = H.subgraph(nodes)

physicsRichClubCoefs = nx.rich_club_coefficient(computerSubgraph,normalized=True, Q=10, seed=128)

nodes = (
    node
    for node, data
    in G.nodes(data=True)
    if data.get("field") == "Agricultural and Biological Sciences"
)
agriculturalSubgraph = H.subgraph(nodes)

agriculturalRichClubCoefs = nx.rich_club_coefficient(agriculturalSubgraph,normalized=True, Q=10, seed=125)

nodes = (
    node
    for node, data
    in G.nodes(data=True)
    if data.get("field") == "Biochemistry, Genetics and Molecular Biology"
)
biochemistrySubgraph = H.subgraph(nodes)

biochemistryRichClubCoefs = nx.rich_club_coefficient(biochemistrySubgraph,normalized=True, Q=10, seed=125)

richClubCoefs = pd.DataFrame(columns=[])

richClubCoefs["Computer Science"] = computerRichClubCoefs.values()
richClubCoefs["Physics and Astronomy"] = physicsRichClubCoefs.values()
richClubCoefs["Agricultural and Biological Sciences"] = agriculturalRichClubCoefs.values()
richClubCoefs["Biochemistry, Genetics and Molecular Biology"] = biochemistryRichClubCoefs.values()

richClubCoefs.to_csv("richClubCoefs.csv", index=False)
