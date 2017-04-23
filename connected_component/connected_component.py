"""
Determine, whether a given graph is connected.

Author: Christopher Gondek
"""


def edges_to_graph(input_edges):
    """Converts a list of edges into a graph.
    Vertices without an edge are not considered.
    
    Parameters
    ----------
    input_edges : list of tuples (a, b)
        List of edges.
        
    Returns
    -------
    dict
        A graph as dict, each node is once key with a set of adjacent knots as value.
    """

    graph = dict()
    for a, b in input_edges:
        if a in graph:
            graph[a].add(b)
        else:
            s = set()
            s.add(b)
            graph[a] = s
        if b in graph:
            graph[b].add(a)
        else:
            s = set()
            s.add(a)
            graph[b] = s

    return graph


def is_connected(result_graph):
    """Determines, whether all vertices that contain an edge are connected.
    Vertices without an edge are not considered.
    
    Parameters
    ----------
    result_graph : dict
        A graph as returned by edges_to_graph.
        
    Returns
    -------
    bool
        True, if the graph is connected.
    """

    visited = set()
    stack = []
    start = next(iter(result_graph.keys()))
    stack.append(start)
    visited.add(start)

    while stack:
        node = stack.pop()
        visited.add(node)
        if node not in result_graph:
            continue
        for adjacent_node in result_graph[node]:
            if adjacent_node not in visited:
                stack.append(adjacent_node)

    if len(result_graph) == len(visited):
        return True
    else:
        return False

if __name__ == "__main__":
    edges = [
        (1, 2),
        (1, 2),
        (2, 1),
        (1, 3),
        (2, 3),
        (3, 4),
        (4, 5),
        (9, 10)
    ]

    graph = edges_to_graph(edges)
    print(graph)

    print(is_connected(graph))
