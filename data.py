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

    plt.plot(files, times1, marker = "o", label = "adjacency_dict_cycles") # Change Name of the Func
    plt.plot(files, times2, marker = "o", label = "adjacency_matrix_cycles") # Change Name of the Func
    plt.title("Comparing time execution for different data sizes")
    plt.xlabel(".dot files (name for number of nodes)")
    plt.ylabel("Execution time (s)")
    plt.grid(True)
    plt.legend()
    plt.show()

d = ["50.dot", "80.dot", "110.dot", "140.dot", "170.dot", "200.dot", "230.dot"]

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
