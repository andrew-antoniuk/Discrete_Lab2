""" Desc """

import time
import matplotlib.pyplot as plt
import lab

def measure(read_fn1, f1, read_fn2, f2, files: list):

    """
    Compare two algorithms on the same dataset and plot both curves.
    """

    times1, times2 = [], []

    for f in files:
        data = read_fn1(f)
        start = time.time()
        f1(data)
        # f1(data, 0)
        times1.append(time.time() - start)
    for f in files:
        data = read_fn2(f)
        start = time.time()
        f2(data)
        # f2(data, 0)
        times2.append(time.time() - start)

    plt.plot(files, times1, marker = "o", label = "iterative_adjacency_dict_dfs")
    plt.plot(files, times2, marker = "o", label = "iterative_adjacency_matrix_dfs")
    plt.title("Comparing")
    plt.xlabel("Graph files (50-170 nodes)")
    plt.ylabel("Execution time (s)")
    plt.grid(True)
    plt.legend()
    plt.show()

d = ["g1.dot", "g2.dot", "g3.dot", "g4.dot", "g5.dot", "g6.dot", "g7.dot"]

# measure(
#     lab.read_adjacency_dict,
#     lab.iterative_adjacency_dict_dfs,
#     lab.read_adjacency_matrix,
#     lab.iterative_adjacency_matrix_dfs,
#     d
# )

# measure(
#     lab.read_adjacency_dict,
#     lab.iterative_adjacency_dict_bfs,
#     lab.read_adjacency_matrix,
#     lab.iterative_adjacency_matrix_bfs,
#     d
# )

# measure(
#     lab.read_adjacency_dict,
#     lab.recursive_adjacency_dict_dfs,
#     lab.read_adjacency_matrix,
#     lab.recursive_adjacency_matrix_dfs,
#     d
# )

# measure(
#     lab.read_adjacency_matrix,
#     lab.adjacency_matrix_radius,
#     lab.read_adjacency_dict,
#     lab.adjacency_dict_radius,
#     d
# )

# measure(
#     lab.read_adjacency_dict,
#     lab.adjacency_dict_cycles,
#     lab.read_adjacency_matrix,
#     lab.adjacency_matrix_cycles,
#     d
# )
