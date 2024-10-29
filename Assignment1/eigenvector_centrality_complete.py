import numpy as np
import networkx as nx
import sys


def import_graph(data):
    edges = eval(f"[{data}]")
    G = nx.Graph()
    G.add_edges_from(edges)
    return G


def eigenvector_centrality(graph, max_iter=100):
    """
    Calculate the Eigenvector Centrality of a given graph using the power iteration method.

    Parameters:
     - graph: A NetworkX graph
     - max_iter: Maximum number of iterations

    Returns:
     - A dictionary with nodes as keys and their eigenvector centrality as values.

    """
    centrality_dict = {node: 0 for node in graph}

    # Get the adjacency matrix of the graph
    adjacency_matrix = nx.to_numpy_array(graph)
    n = adjacency_matrix.shape[0]  # Number of nodes

    centrality = np.ones(n) / n

    for i in range(max_iter):
        new_centrality = np.dot(adjacency_matrix, centrality)
        new_centrality /= np.linalg.norm(new_centrality, 2)

        centrality = new_centrality

    nodes = list(graph.nodes())
    centrality_dict = {nodes[i]: centrality[i] for i in range(n)}

    return centrality_dict


if __name__ == "__main__":

    data = sys.stdin.read()
    G = import_graph(data)

    centrality = eigenvector_centrality(G)

    print("Eigenvector Centralitys of the graph")
    for node, value in centrality.items():
        print(f"Node {node}: {value:.4f}")
