import sys
import networkx as nx
import matplotlib.pyplot as plt


def import_graph(data):
    edges = eval(f"[{data}]")
    G = nx.Graph()
    G.add_edges_from(edges)
    return G


def hits(graph, max_iter=100):
    """
    Implement the HITS algorithm for a directed graph.

    Parameters:
    - graph: A NetworkX graph (directed).
    - max_iter: Maximum number of iterations (default=100).
    - tol: Tolerance to check convergence (default=1.0e-8).

    Returns:
    - (authorities, hubs): A tuple of two dictionaries with node authority and hub scores.
    """

    # Initialize authority and hub scores to 1
    nodes = list(graph.nodes())
    n = len(nodes)
    auth = dict.fromkeys(nodes, 1.0)
    hubs = dict.fromkeys(nodes, 1.0)

    for i in range(max_iter):
        # Update authority scores
        old_auth = auth.copy()
        for node in graph:
            auth[node] = sum(hubs[neighbor] for neighbor in graph.predecessors(node))

        # Update hub scores
        old_hubs = hubs.copy()
        for node in graph:
            hubs[node] = sum(auth[neighbor] for neighbor in graph.successors(node))

        # Normalize authority and hub scores
        norm_auth = sum(auth.values())
        norm_hubs = sum(hubs.values())
        auth = {node: score / norm_auth for node, score in auth.items()}
        hubs = {node: score / norm_hubs for node, score in hubs.items()}

    return auth, hubs


if __name__ == "__main__":
    data = sys.stdin.read()
    G = import_graph(data)
    auths, hubs = hits(G)

    print("Authority Scores of the graph:")
    for node, score in auths.items():
        print(f"Node {node}: {score:.4f}")

    print("\nHub Scores of the graph:")
    for node, score in hubs.items():
        print(f"Node {node}: {score:.4f}")
