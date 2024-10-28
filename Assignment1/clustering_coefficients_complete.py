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

    for node in graph:
        neighbors = list(graph.neighbors(node))
        k = len(neighbors)  # Number of neighbors

        if k < 2:
            # If a node has fewer than 2 neighbors, clustering coefficient is 0
            clustering_coeffs[node] = 0.0
        else:
            # Count the number of edges between neighbors
            subgraph = graph.subgraph(neighbors)
            actual_edges = subgraph.number_of_edges()

            # Clustering coefficient formula
            clustering_coeffs[node] = 2 * actual_edges / (k * (k - 1))

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

    for node in graph:
        neighbors = list(graph.neighbors(node))
        k = len(neighbors)  # Number of neighbors

        if k >= 2:
            # Count the number of edges between neighbors
            subgraph = graph.subgraph(neighbors)
            actual_edges = subgraph.number_of_edges()

            # Update the counts for global clustering coefficient
            total_closed_triplets += actual_edges
            total_triplets += k * (k - 1) / 2

    # Calculate the global clustering coefficient (transitivity)
    if total_triplets > 0:
        return total_closed_triplets / total_triplets
    else:
        return 0.0


if __name__ == "__main__":
    data = sys.stdin.read()
    G = import_graph(data)
    clustering_coeff, global_coeff = local_clustering_coefficent(
        G
    ), global_clustering_coefficient(G)

    print("Global Clustering Coefficent of the graph")
    print(global_coeff)

    print("Local Clustering Coefficients of the graph:")
    for node, coeff in clustering_coeff.items():
        print(f"Node {node}: {coeff:.4f}")
