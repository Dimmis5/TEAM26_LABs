
def is_valid_labeling(labeling, graph):

    for node in graph:
        for neighbor in graph[node]:
            if labeling[node] == labeling[neighbor]:
                return False
    return True


def can_use_label(node, label, labeling, graph):

    for neighbor in graph[node]:
        if labeling[neighbor] == label:
            return False
    return True


def assign_labels(k, graph):

    n = len(graph)
    labeling = [-1] * n

    def backtrack(index):
        if index == n:
            return True

        node = index

        for label in range(k):
            if can_use_label(node, label, labeling, graph):
                labeling[node] = label

                if backtrack(index + 1):
                    return True

                labeling[node] = -1

        return False

    success = backtrack(0)
    return success, labeling


def find_min_labels(graph):

    n = len(graph)

    for k in range(1, n + 1):
        success, labeling = assign_labels(k, graph)

        if success:
            return k, labeling

    return None, []
graph4 = {
    0: [1, 2, 3],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [0, 1, 2]
}

print("Graph")
print(find_min_labels(graph4))