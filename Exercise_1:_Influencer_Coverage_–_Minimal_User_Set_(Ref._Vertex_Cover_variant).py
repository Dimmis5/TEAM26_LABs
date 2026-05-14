def is_valid_coverage(selected_users, graph):
    n = len(graph)
    is_covered = [False] * n
    for user_id in selected_users:
        is_covered[user_id] = True
        for neighbor in graph[user_id]:
            is_covered[neighbor] = True
    return all(is_covered)

def find_minimum_coverage(graph):
    n = len(graph)
    best_size = n + 1
    best_subset = []
    for i in range(1, 1 << n):
        current_subset = []
        for bit in range(n):
            if (i >> bit) & 1:
                current_subset.append(bit)
        current_size = len(current_subset)
        if current_size < best_size:
            if is_valid_coverage(current_subset, graph):
                best_size = current_size
                best_subset = current_subset
    return (best_size, best_subset)

def find_fast_coverage():
    n = len(graph) 
    uncovered_nodes = set(range(n))
    selected_users = []
    while uncovered_nodes:
        best_node = -1
        max_new_coverage = -1
        for potential_node in range(n):
            count = 0
            if potential_node in uncovered_nodes:
                count += 1
            for neighbor in graph[potential_node]:
                if neighbor in uncovered_nodes:
                    count += 1
            if count > max_new_coverage:
                max_new_coverage = count
                best_node = potential_node
        selected_users.append(best_node)
        uncovered_nodes.discard(best_node)
        for neighbor in graph[best_node]:
            uncovered_nodes.discard(neighbor)
    return (len(selected_users), selected_users)

if __name__ == "__main__":

    graph = {
        0: [1],
        1: [0, 2],
        2: [1, 3, 4],
        3: [2],
        4: [2]
    }
    

    test_users = [2]
    valid = is_valid_coverage(test_users, graph)
    print(f"Verification de {test_users} : {valid}") 

    exact_size, exact_list = find_minimum_coverage(graph)
    print(f"Exact Solution (Brute Force): Size {exact_size}, users {exact_list}")
    
    greedy_size, greedy_list = find_fast_coverage()
    print(f"Quick Solution (Greedy): Size {greedy_size}, users {greedy_list}")