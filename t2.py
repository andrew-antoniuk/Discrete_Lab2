""" Тести 2 """


def eccentricity_matrix_adj(graph: list[list[int]], start: int) -> int:

    """
    Searches for the eccentricity of the vertex
    in the graph represented as an incidence matrix

    M[inc] = {0, 1}
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



g = {
    'A': ['B', 'C', 'D'], #0
    'B': ['A', 'C', 'E', 'J'], #1
    'C': ['A', 'B', 'E', 'D', 'J'], #1
    'D': ['A', 'C', 'G'], #1
    'E': ['B', 'C', 'F', 'H'], #2
    'F': ['E', 'I', 'J'], #3
    'G': ['D', 'J', 'H'], #2
    'H': ['E', 'G', 'I'], #3
    'I': ['F', 'H'], #4
    'J': ['B', 'C', 'F', 'G'] #2
}

g_adj = [
#    A B C D E F G H I J
    [0,1,1,1,0,0,0,0,0,0], # A
    [1,0,1,0,1,0,0,0,0,1], # B
    [1,1,0,1,1,0,0,0,0,1], # C
    [1,0,1,0,0,0,1,0,0,0], # D
    [0,1,1,0,0,1,0,1,0,0], # E
    [0,0,0,0,1,0,0,0,1,1], # F
    [0,0,0,1,0,0,0,1,0,1], # G
    [0,0,0,0,1,0,1,0,1,0], # H
    [0,0,0,0,0,1,0,1,0,0], # I
    [0,1,1,0,0,1,1,0,0,0]  # J
]

g_inc = [
#    0, 1  2  3  4  5  6  7  8  9  10 a  b  c  d  f
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # A
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # B
    [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], # C
    [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], # D
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0], # E
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0], # F
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0], # G
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1], # H
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1], # I
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0]  # J
]

h = {
    'A': ['B', 'C', 'D'], #0
    'B': ['A', 'C', 'E', 'J'], #1
    'C': ['A', 'B', 'E', 'D', 'J'], #1
    'D': ['A', 'C'], #1
    'E': ['B', 'C'], #2
    'J': ['B', 'C'] #2
}

h_adj = [
#    A B C D E J
    [0,1,1,1,0,0], # A
    [1,0,1,0,1,1], # B
    [1,1,0,1,1,1], # C
    [1,0,1,0,0,0], # D
    [0,1,1,0,0,0], # E
    [0,1,1,0,0,0]  # J
]

h_inc = [
#    1  2  3  4  5  6  7  8
    [1, 1, 1, 0, 0, 0, 0, 0], # A
    [1, 0, 0, 1, 1, 0, 0, 0], # B
    [0, 1, 0, 0, 0, 1, 1, 1], # C
    [0, 0, 1, 0, 0, 1, 0, 0], # D
    [0, 0, 0, 1, 0, 0, 1, 0], # E
    [0, 0, 0, 0, 1, 0, 0, 1]  # J
]

# print(eccentricity_matrix_adj(g_adj, 0))
# print(eccentricity_matrix_adj(g_adj, 1))
# print(eccentricity_matrix_adj(g_adj, 2))
# print(eccentricity_matrix_adj(g_adj, 3))
# print(eccentricity_matrix_adj(g_adj, 4))
# print(eccentricity_matrix_adj(g_adj, 5))
# print(eccentricity_matrix_adj(g_adj, 6))
# print(eccentricity_matrix_adj(g_adj, 7))
# print(eccentricity_matrix_adj(g_adj, 8))
# print(eccentricity_matrix_adj(g_adj, 9))
# print(bfs_eccentricity_dict(g, "A"))
# print(eccentricity_dict(h, "A"))
# print(bfs_dict(g, "A"))
# print(recursive_adjacency_dict_dfs(graph, "F"))
# print(recursive_adjacency_matrix_dfs(graph, "F"))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
