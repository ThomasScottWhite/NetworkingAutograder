import sys
import networkx as nx
import matplotlib.pyplot as plt


def import_graph(data):
    edges = eval(f"[{data}]")
    G = nx.Graph()
    G.add_edges_from(edges)
    return G


def HITS(Graph):
    pass


if __name__ == "__main__":
    data = sys.stdin.read()
    G = import_graph(data)
    HITS(G)
