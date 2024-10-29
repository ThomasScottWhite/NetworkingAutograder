import sys
import networkx as nx
import matplotlib.pyplot as plt


def import_graph(data):
    edges = eval(f"[{data}]")
    G = nx.Graph()
    G.add_edges_from(edges)
    return G


def local_clustering_coefficent(graph):
    """
    Calculate the clustering coefficient for each node in the graph.

    Parameters:
    - graph: A NetworkX graph (undirected).

    Returns:
    - A dictionary with node clustering coefficients.
    """
    nodes = list(graph.nodes())
    clustering_coeffs = dict.fromkeys(nodes, 0)
    # Implement here

    return clustering_coeffs


def global_clustering_coefficient(graph):
    """
    Calculate the global clustering coefficient (transitivity) of the graph.

    Parameters:
    - graph: A NetworkX graph (undirected).

    Returns:
    - The global clustering coefficient.
    """
    total_closed_triplets = 0
    total_triplets = 0

    # Implement here

    if total_triplets > 0:
        return total_closed_triplets / total_triplets
    else:
        return 0.0


if __name__ == "__main__":
    data = sys.stdin.read()
    G = import_graph(data)

    clustering_coeff = local_clustering_coefficent(G)
    global_coeff = global_clustering_coefficient(G)
    
    print("Global Clustering Coefficent of the graph")
    print(global_coeff)

    print("Local Clustering Coefficients of the graph:")
    for node, coeff in clustering_coeff.items():
        print(f"Node {node}: {coeff:.4f}")
