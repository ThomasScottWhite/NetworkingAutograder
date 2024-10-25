import sys
import networkx as nx
import matplotlib.pyplot as plt


def import_graph(data):
    edges = eval(f"[{data}]")
    G = nx.Graph()
    G.add_edges_from(edges)
    return G


def page_rank(graph, damping=0.85, max_iterations=100):
    """
    Compute PageRank from scratch using the power iteration method.

    Parameters:
    - graph: dict, adjacency list representation of the graph
    - damping: float, damping factor (default 0.85)
    - max_iterations: int, maximum number of iterations

    Returns:
    - PageRank: dict, containing nodes and their PageRank scores
    """
    # Number of nodes in the graph
    N = len(graph)

    # Initialize PageRank for each node (1/N)
    pagerank = {node: 1 / N for node in graph}

    for iteration in range(max_iterations):
        pass
        # Implement Pagerank

    return pagerank


if __name__ == "__main__":
    data = sys.stdin.read()
    G = import_graph(data)
    page_rank_dict = page_rank(G)

    print("PageRank of the graph:")
    for node, rank in page_rank_dict.items():
        print(f"Node {node}: {rank:.4f}")
