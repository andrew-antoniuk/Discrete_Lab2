"""
Lab 2 by Taras Konoval & Antoniuk Andrii
"""

def read_incidence_matrix(filename: str) -> list[list[int]]:
    """
    :param str filename: path to file
    :returns list[list[int]]: the incidence matrix of a given graph
    """
    edges = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if "->" in line:
                left, right = line.split("->")
                u = int(left.strip())
                v = int(right.strip().strip(";"))
                edges.append((u, v))

    max_vertex = 0
    for u, v in edges:
        max_vertex = max(max_vertex, u, v)

    n = max_vertex + 1
    m = len(edges)

    matrix = [[0 for _ in range(m)] for _ in range(n)]

    for j, (u, v) in enumerate(edges):
        if u == v:
            matrix[u][j] = 2
        else:
            matrix[u][j] = 1
            matrix[v][j] = -1

    return matrix


def read_adjacency_matrix(filename: str) -> list[list[int]]:
    """
    :param str filename: path to file
    :returns list[list[int]]: the adjacency matrix of a given oriented graph
    """
    edges = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if "->" in line:
                left, right = line.split("->")
                u = int(left.strip())
                v = int(right.strip().strip(";"))
                edges.append((u, v))

    max_vertex = 0
    for u, v in edges:
        max_vertex = max(max_vertex, u, v)

    n = max_vertex + 1

    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for u, v in edges:
        matrix[u][v] = 1

    return matrix


def read_adjacency_dict(filename: str) -> dict[int, list[int]]:
    """
    :param str filename: path to file
    :returns dict[int, list[int]]: the adjacency dict of a given oriented graph
    """
    edges = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if "->" in line:
                left, right = line.split("->")
                u = int(left.strip())
                v = int(right.strip().strip(";"))
                edges.append((u, v))

    max_vertex = 0
    for u, v in edges:
        max_vertex = max(max_vertex, u, v)

    n = max_vertex + 1

    graph = {i: [] for i in range(n)}

    for u, v in edges:
        graph[u].append(v)

    return graph


def iterative_adjacency_dict_dfs(graph: dict[int, list[int]], start: int) -> list[int]:

    """
    :param dict[int, list[int]] graph: the adjacency list of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> iterative_adjacency_dict_dfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0)
    [0, 1, 2]
    >>> iterative_adjacency_dict_dfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0)
    [0, 1, 2, 3]
    """

    pass


def iterative_adjacency_matrix_dfs(graph: list[list[int]], start: int) -> list[int]:

    """
    :param list[list[int]] graph: the adjacency matrix of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> iterative_adjacency_matrix_dfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
    [0, 1, 2]
    >>> iterative_adjacency_matrix_dfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0)
    [0, 1, 2, 3]
    """

    pass


def recursive_adjacency_dict_dfs(graph: dict[int, list[int]],
                                 start: int,
                                 visited = None) -> list[int]:

    """
    :param dict[int, list[int]] graph: the adjacency list of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> recursive_adjacency_dict_dfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0)
    [0, 1, 2]
    >>> recursive_adjacency_dict_dfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0)
    [0, 1, 2, 3]
    """

    if visited is None:
        visited = []

    visited.append(start)

    for vert in graph[start]:
        if vert not in visited:
            recursive_adjacency_dict_dfs(graph, vert, visited)

    return visited


def recursive_adjacency_matrix_dfs(graph: list[list[int]], start: int, visited = None) -> list[int]:

    """
    :param list[list[int]] graph: the adjacency matrix of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> recursive_adjacency_matrix_dfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
    [0, 1, 2]
    >>> recursive_adjacency_matrix_dfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0)
    [0, 1, 2, 3]
    """

    if visited is None:
        visited = []

    visited.append(start)

    for index, val in enumerate(graph[start]):
        if val == 1 and index not in visited:
            recursive_adjacency_matrix_dfs(graph, index, visited)

    return visited


def iterative_adjacency_dict_bfs(graph: dict[int, list[int]], start: int) -> list[int]:

    """
    :param dict[int, list[int]] graph: the adjacency list of a given graph
    :param int start: start vertex of search
    :returns list[int]: the bfs traversal of the graph
    >>> iterative_adjacency_dict_bfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0)
    [0, 1, 2]
    >>> iterative_adjacency_dict_bfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0)
    [0, 1, 2, 3]

    """

    pass


def iterative_adjacency_matrix_bfs(graph: list[list[int]], start: int) -> list[int]:

    """
    :param list[list[int]] graph: the adjacency matrix of a given graph
    :param int start: start vertex of search
    :returns list[int]: the bfs traversal of the graph
    >>> iterative_adjacency_matrix_bfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
    [0, 1, 2]
    >>> iterative_adjacency_matrix_bfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0)
    [0, 1, 2, 3]
    """

    pass


def adjacency_matrix_radius(graph: list[list[int]]) -> int:

    """
    :param list[list[int]] graph: the adjacency matrix of a given graph
    :returns int: the radius of the graph
    >>> adjacency_matrix_radius([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    1
    >>> adjacency_matrix_radius([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 1, 0, 0]])
    1
    """

    pass


def adjacency_dict_radius(graph: dict[int, list[int]]) -> int:

    """
    :param dict[int, list[int]] graph: the adjacency list of a given graph
    :returns int: the radius of the graph
    >>> adjacency_dict_radius({0: [1, 2], 1: [0, 2], 2: [0, 1]})
    1
    >>> adjacency_dict_radius({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: [1]})
    1
    """

    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
