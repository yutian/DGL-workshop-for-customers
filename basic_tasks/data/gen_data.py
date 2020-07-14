import networkx as nx
import torch
import scipy.sparse as sp
import pandas as pd
import numpy as np
import random

g = nx.karate_club_graph().to_undirected().to_directed()
ids = []
clubs = []
ages = []
for nid, attr in g.nodes(data=True):
    ids.append(nid)
    clubs.append(attr['club'])
    ages.append(random.randint(30, 50))
nodes = pd.DataFrame({'Id' : ids, 'Club' : clubs, 'Age' : ages})
print(nodes)
src = []
dst = []
weight = []
for u, v in g.edges():
    src.append(u)
    dst.append(v)
    weight.append(random.random())
edges = pd.DataFrame({'Src' : src, 'Dst' : dst, 'Weight' : weight})
print(edges)

nodes.to_csv('nodes.csv', index=False)
edges.to_csv('edges.csv', index=False)

