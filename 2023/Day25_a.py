from itertools import combinations
import networkx as nx

with open("files/day25.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

G = nx.Graph()
for line in lines:
    node, neighbors = line.split(': ')
    neighbors = neighbors.split(' ')
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

edges = nx.minimum_edge_cut(G)

for edge in edges:
    G.remove_edge(edge[0], edge[1])

first, second = list(nx.connected_components(G))
print(len(first) * len(second))