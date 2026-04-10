def dfs_recursive(graph, start, visited, component):
    visited.add(start)
    component.append(start)
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, component)


def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            result.append(v)
            for u in graph.get(v, []):
                if u not in visited:
                    stack.append(u)
    return result


def find_connected_components(graph):
    visited = set()
    components = []

    for user in graph:
        if user not in visited:
            component = []
            dfs_recursive(graph, user, visited, component)
            components.append(component)
    return components


def is_connected(graph):
    if not graph:
        return False
    return len(find_connected_components(graph)) == 1

def has_path(graph, start, target):
    if start == target:
        return True

    visited = set()
    stack = [start]

    while stack:
        user = stack.pop()
        if user == target:
            return True
        if user not in visited:
            visited.add(user)
            for friend in graph.get(user, []):
                if friend not in visited:
                    stack.append(friend)
    return False


def get_connected_components_sizes(graph):
    return [len(c) for c in find_connected_components(graph)]


def find_largest_component(graph):
    components = find_connected_components(graph)
    largest = []
    for comp in components:
        if len(comp) > len(largest):
            largest = comp
    return largest


def find_isolated_users(graph):
    return [user for user in graph if len(graph.get(user, [])) == 0]



# test cases
graph1 = {
    "Alice": ["Bob", "Charlie"],
    "Bob": ["Alice", "David"],
    "Charlie": ["Alice"],
    "David": ["Bob"],
    "Eve": ["Frank"],
    "Frank": ["Eve"],
    "Grace": [],
}

graph2 = {"Solo": []}
graph3 = {}
graph4 = {"X": [], "Y": []}
graph5 = {"A": ["B"], "B": ["A", "C"], "C": ["B", "D"], "D": ["C"]}

# dfs_recursive
v, c = set(), []
dfs_recursive(graph1, "Alice", v, c)
print("dfs_recursive normal         :", c)

v, c = set(), []
dfs_recursive(graph2, "Solo", v, c)
print("dfs_recursive single node    :", c)

# dfs_iterative
print("dfs_iterative normal         :", dfs_iterative(graph1, "Alice"))
print("dfs_iterative single node    :", dfs_iterative(graph2, "Solo"))
print("dfs_iterative empty graph    :", dfs_iterative(graph3, "A") if graph3 else [])

# find_connected_components
print("components normal            :", [sorted(c) for c in find_connected_components(graph1)])
print("components single node       :", find_connected_components(graph2))
print("components empty graph       :", find_connected_components(graph3))

# is_connected
print("is_connected normal          :", is_connected(graph1))
print("is_connected single node     :", is_connected(graph2))
print("is_connected empty graph     :", is_connected(graph3))
print("is_connected disconnected    :", is_connected(graph4))

# has_path
print("has_path existing path       :", has_path(graph1, "Alice", "David"))
print("has_path across components   :", has_path(graph1, "Alice", "Eve"))
print("has_path isolated node       :", has_path(graph1, "Grace", "Alice"))
print("has_path same node           :", has_path(graph1, "Alice", "Alice"))
print("has_path chain end to end    :", has_path(graph5, "A", "D"))

# get_connected_components_sizes
print("sizes normal                 :", sorted(get_connected_components_sizes(graph1)))
print("sizes empty graph            :", get_connected_components_sizes(graph3))

# find_largest_component
print("largest normal               :", sorted(find_largest_component(graph1)))
print("largest empty graph          :", find_largest_component(graph3))

# find_isolated_users
print("isolated normal              :", find_isolated_users(graph1))
print("isolated single node         :", find_isolated_users(graph2))
print("isolated empty graph         :", find_isolated_users(graph3))