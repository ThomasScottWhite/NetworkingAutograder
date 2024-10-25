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
    - tol: float, tolerance for convergence

    Returns:
    - PageRank: dict, containing nodes and their PageRank scores
    """
    # Number of nodes in the graph
    N = len(graph)

    # Initialize PageRank for each node (1/N)
    pagerank = {node: 1 / N for node in graph}

    for iteration in range(max_iterations):
        new_pagerank = {}
        for node in graph:

            # Calculate the rank from incoming links
            rank_sum = sum(
                pagerank[neighbor] / len(graph[neighbor])
                for neighbor in graph
                if node in graph[neighbor]
            )

            # Apply the PageRank formula
            new_pagerank[node] = (1 - damping) / N + damping * rank_sum

        pagerank = new_pagerank

    return pagerank


if __name__ == "__main__":
    data = sys.stdin.read()
    G = import_graph(data)
    page_rank_dict = page_rank(G)

    print("PageRank of the graph:")
    for node, rank in page_rank_dict.items():
        print(f"Node {node}: {rank:.4f}")
