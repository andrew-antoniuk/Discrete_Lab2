"""
Lab 2 by Taras Konoval & Antoniuk Andrii
"""

#####################
#   1. Graph Read   #
#####################

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


##############################
#   2. DFS & BFS Iterative   #
##############################


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

    visited = set()
    stack = [start]
    order = []

    while stack:
        v = stack.pop()

        if v not in visited:
            visited.add(v)
            order.append(v)

            for neighbor in reversed(graph[v]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return order


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
    visited = set()
    stack = [start]
    order = []

    n = len(graph)

    while stack:
        v = stack.pop()

        if v not in visited:
            visited.add(v)
            order.append(v)

            for node in range(n - 1, -1, -1):
                if graph[v][node] == 1 and node not in visited:
                    stack.append(node)

    return order


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
    visited = set()
    stack = [start]
    order = []

    visited.add(start)

    while stack:
        v = stack.pop(0)
        order.append(v)

        for node in graph[v]:
            if node not in visited:
                visited.add(node)
                stack.append(node)

    return order


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

    visited = set()
    stack = [start]
    order = []

    visited.add(start)
    n = len(graph)

    while stack:
        v = stack.pop(0)
        order.append(v)

        for node in range(n):
            if graph[v][node] == 1 and node not in visited:
                visited.add(node)
                stack.append(node)

    return order


########################
#   3. DFS Recursive   #
########################

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


#######################
#   4. Graph Radius   #
#######################

def eccentricity_matrix_adj(graph: list[list[int]], start: int) -> int:

    """
    Searches for the eccentricity of the vertex
    in the graph represented as an adjacency matrix
    by BFS-method

    :param list[list[int]] graph: the adjacency matrix of a given graph
    :param int start: start vertex of search
    :returns int: eccentricity of the vertex in the graph

    M[adj] = {0, 1}
    """

    stack = [(start, 0)]
    visited = {start}
    max_dis = 0

    while stack:
        node_cur, dis_cur = stack.pop(0)
        max_dis = max(max_dis, dis_cur)

        for index, node in enumerate(graph[node_cur]):
            if node == 1 and index not in visited:
                dis_new = dis_cur + 1
                visited.add(index)
                stack.append((index, dis_new))

    return max_dis


def adjacency_matrix_radius(graph: list[list[int]]) -> int:

    """
    :param list[list[int]] graph: the adjacency matrix of a given graph
    :returns int: the radius of the graph
    >>> adjacency_matrix_radius([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    1
    >>> adjacency_matrix_radius([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 1, 0, 0]])
    1
    """

    eccentricities = {eccentricity_matrix_adj(graph, vert) for vert, _ in enumerate(graph)}
    return min(eccentricities)


def eccentricity_dict(graph: dict[list[list[int]]], start: int) -> int:

    """
    Searches for the eccentricity of the vertex
    in the graph represented as dictionary
    by BFS-method

    :param dict[list[list[int]]] graph: graph represented as a dictionary
    :param int start: start vertex of search
    :returns int: eccentricity of the vertex in the graph
    """

    stack = [(start, 0)]
    visited = {start}
    max_dis = 0

    while stack:
        node_cur, dis_cur = stack.pop(0)
        max_dis = max(max_dis, dis_cur)

        if node_cur in graph:
            for node in graph[node_cur]:
                if node not in visited:
                    dis_new = dis_cur + 1
                    visited.add(node)
                    stack.append((node, dis_new))

    return max_dis


def adjacency_dict_radius(graph: dict[int, list[int]]) -> int:

    """
    :param dict[int, list[int]] graph: the adjacency list of a given graph
    :returns int: the radius of the graph
    >>> adjacency_dict_radius({0: [1, 2], 1: [0, 2], 2: [0, 1]})
    1
    >>> adjacency_dict_radius({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: [1]})
    1
    """

    eccentricities = {eccentricity_dict(graph, vert) for vert in graph}
    return min(eccentricities)


#######################
#   5. Graph Cycles   #
#######################

def dfs_find_cycles(graph, start, v, path, on_path, cycles):

    """
    Performs a DFS to find all simple directed cycles that start at `start`.

    >>> graph = {0: [1], 1: [0]}
    >>> cycles = []
    >>> dfs_find_cycles(graph, 0, 0, [0], {0}, cycles)
    >>> cycles
    [[0, 1]]

    >>> graph = {0: [1], 1: [2], 2: [0]}
    >>> cycles = []
    >>> dfs_find_cycles(graph, 0, 0, [0], {0}, cycles)
    >>> cycles
    [[0, 1, 2]]
    """

    for node in graph[v]:
        if node == start:

            if len(path) > 0:
                cycles.append(path.copy())

        elif node not in on_path and node >= start:
            on_path.add(node)
            path.append(node)

            dfs_find_cycles(graph, start, node, path, on_path, cycles)

            path.pop()
            on_path.remove(node)


def adjacency_dict_cycles(graph: dict[int, list[int]]) -> list[list[int]]:

    """
    Finds all unique simple directed cycles in a graph represented
    as an adjacency dictionary.

    >>> adjacency_dict_cycles({0: [1], 1: [0]})
    [[0, 1]]

    >>> adjacency_dict_cycles({0: [1], 1: [2], 2: [0]})
    [[0, 1, 2]]

    >>> adjacency_dict_cycles({0: [1,2], 1: [0,2], 2: [0,1]})
    [[0, 1], [0, 1, 2], [0, 2], [0, 2, 1], [1, 2]]
    """

    cycles = []
    vertices = sorted(graph.keys())

    for start in vertices:
        dfs_find_cycles(
            graph=graph,
            start=start,
            v=start,
            path=[start],
            on_path={start},
            cycles=cycles
        )

    unique_cycles = []
    seen = set()

    for cycle in cycles:
        m = min(cycle)
        idx = cycle.index(m)
        rotated = cycle[idx:] + cycle[:idx]
        key = tuple(rotated)

        if key not in seen:
            seen.add(key)
            unique_cycles.append(rotated)

    return unique_cycles

def adjacency_matrix_cycles(graph: list[list[int]]) -> list[list[int]]:

    """
    Finds all unique simple directed cycles in a graph represented
    as an adjacency matrix.

    >>> adjacency_matrix_cycles([[0,1],[1,0]])
    [[0, 1]]

    >>> adjacency_matrix_cycles([
    ...     [0,1,0],
    ...     [0,0,1],
    ...     [1,0,0]
    ... ])
    [[0, 1, 2]]

    >>> adjacency_matrix_cycles([
    ...     [0,1,1],
    ...     [1,0,1],
    ...     [1,1,0]
    ... ])
    [[0, 1], [0, 1, 2], [0, 2], [0, 2, 1], [1, 2]]
    """

    n = len(graph)
    adj = {i: [] for i in range(n)}

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                adj[i].append(j)

    return adjacency_dict_cycles(adj)


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
