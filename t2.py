""" Тести 2 """

def recursive_adjacency_dict_dfs(graph: dict[int, list[int]],
                                 start: int,
                                 path = None) -> list[int]:

    """
    :param dict[int, list[int]] graph: the adjacency list of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> recursive_adjacency_dict_dfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0)
    [0, 1, 2]
    >>> recursive_adjacency_dict_dfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0)
    [0, 1, 2, 3]
    """

    # if path is None:
    #     path = []

    # if stack is None:
    #     stack = set()

    # path.append(start)

    # s = set(graph[start]) - set(path)
    # stack.add(start)

    # if not s == set():
    #     n = min(s)
    #     stack.add(n)
    # else:
    #     n = None
    #     stack.discard(start)

    # if len(stack) == 0:
    #     return path
    # return recursive_adjacency_dict_dfs(graph, n, path, stack)

    # if path is None:
    #     path = []

    # if stack is None:
    #     stack = []

    # path.append(start)
    # if start not in stack:
    #     stack.append(start)

    # for vert in graph[start]:
    #     if vert not in path:
    #         return recursive_adjacency_dict_dfs(graph, vert, path)

    if path is None:
        path = []

    path.append(start)

    for vert in graph[start]:
        if vert not in path:
            recursive_adjacency_dict_dfs(graph, vert, path)

    return path


# def recursive_adjacency_matrix_dfs(graph: list[list[int]], start: int) -> list[int]:

#     """
#     :param list[list[int]] graph: the adjacency matrix of a given graph
#     :param int start: start vertex of search
#     :returns list[int]: the dfs traversal of the graph
#     >>> recursive_adjacency_matrix_dfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
#     [0, 1, 2]
#     >>> recursive_adjacency_matrix_dfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0)
#     [0, 1, 2, 3]
#     """

#     pass


# def adjacency_matrix_radius(graph: list[list[int]]) -> int:

#     """
#     :param list[list[int]] graph: the adjacency matrix of a given graph
#     :returns int: the radius of the graph
#     >>> adjacency_matrix_radius([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
#     1
#     >>> adjacency_matrix_radius([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 1, 0, 0]])
#     1
#     """

#     pass

def eccentricity_bfs(graph: dict, vert: str | int) -> int:

    """
    Desc
    """

    dist = {vert: 0}
    stack = [vert]

    while stack:
        v = stack.pop(0)
        for n in graph[v]:
            if n not in dist:
                dist[n] = dist[v] + 1
                stack.append(n)

    return max(dist.values())


# def eccentricity_matrix(graph: dict):

#     """
#     Breadth First Search Method
#     """


def adjacency_dict_radius(graph: dict[int, list[int]]) -> int:

    """
    :param dict[int, list[int]] graph: the adjacency list of a given graph
    :returns int: the radius of the graph
    >>> adjacency_dict_radius({0: [1, 2], 1: [0, 2], 2: [0, 1]})
    1
    >>> adjacency_dict_radius({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: [1]})
    1
    """

    def eccentricity(graph: dict[int, list[int]], vert: int | str) -> int:

        """
        Computes the eccentricity for given vertice in the graph
        """

        return graph, vert

    eccentricities = set()
    for vert in graph:
        eccentricities.add(eccentricity(graph, vert))

    return min(eccentricities)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
