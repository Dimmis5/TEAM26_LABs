import random
import math


def count_cross_edges(groupA, groupB, graph):
    """
    Count the number of edges crossing between groupA and groupB.
    graph is an adjacency list: {node: [neighbors]}
    """
    setB = set(groupB)
    count = 0

    for node in groupA:
        for neighbor in graph[node]:
            if neighbor in setB:
                count += 1

    return count


def create_random_balanced_split(graph):
    """
    Create a random split where each group has at least 40% of all users.
    """
    users = list(graph.keys())
    random.shuffle(users)

    n = len(users)
    min_size = math.ceil(0.4 * n)

    sizeA = random.randint(min_size, n - min_size)

    groupA = users[:sizeA]
    groupB = users[sizeA:]

    return groupA, groupB, min_size


def find_balanced_partition_greedy(graph):
    """
    Start with a random balanced split.
    Then repeatedly move one node if it reduces the number of cross edges.
    Stop when no improvement is possible.
    """
    groupA, groupB, min_size = create_random_balanced_split(graph)

    best_count = count_cross_edges(groupA, groupB, graph)
    improved = True

    while improved:
        improved = False

        for node in list(graph.keys()):
            copyA = groupA.copy()
            copyB = groupB.copy()

            if node in groupA and len(groupA) - 1 >= min_size:
                copyA.remove(node)
                copyB.append(node)

            elif node in groupB and len(groupB) - 1 >= min_size:
                copyB.remove(node)
                copyA.append(node)

            else:
                continue

            new_count = count_cross_edges(copyA, copyB, graph)

            if new_count < best_count:
                best_count = new_count
                groupA = copyA
                groupB = copyB
                improved = True

    return best_count, groupA, groupB


def find_balanced_partition_local_search(graph, iterations):
    """
    Run greedy several times with different random initial splits.
    Keep the best result found.
    """
    best_count = float("inf")
    best_groupA = []
    best_groupB = []

    for _ in range(iterations):
        count, groupA, groupB = find_balanced_partition_greedy(graph)

        if count < best_count:
            best_count = count
            best_groupA = groupA
            best_groupB = groupB

    return best_count, best_groupA, best_groupB

custom_graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B"],
    "D": ["B", "E"],
    "E": ["D", "F"],
    "F": ["E"]
}

count, groupA, groupB = find_balanced_partition_local_search(custom_graph, iterations=100)

print("Custom graph")
print("Cross edges:", count)
print("Group A:", groupA)
print("Group B:", groupB)
print("Sizes:", len(groupA), len(groupB)) 