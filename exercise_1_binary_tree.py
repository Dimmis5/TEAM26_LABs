from collections import deque

class CategoryNode:
    def __init__(self, category_id, name, post_count):
        self.category_id = category_id
        self.name = name
        self.post_count = post_count
        self.left = None
        self.right = None
        self.parent = None

def calculate_height(node):
    if node is None:
        return -1
    return 1 + max(calculate_height(node.left),
                   calculate_height(node.right))

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)

def is_balanced(node):
    if node is None:
        return True
    left = calculate_height(node.left)
    right = calculate_height(node.right)
    if abs(left - right) > 1:
        return False
    return is_balanced(node.left) and is_balanced(node.right)

def is_full_binary_tree(node):
    if node is None:
        return True
    if node.left is None and node.right is None:
        return True
    if node.left and node.right:
        return is_full_binary_tree(node.left) and is_full_binary_tree(node.right)
    return False

def is_perfect_binary_tree(node):
    h = calculate_height(node)
    n = count_nodes(node)
    return n == (2 ** (h + 1) - 1)

def is_complete_binary_tree(node):
    if node is None:
        return True
    queue = deque([node])
    found_null = False
    while queue:
        current = queue.popleft()
        if current is None:
            found_null = True
        else:
            if found_null:
                return False
            queue.append(current.left)
            queue.append(current.right)
    return True

def find_category(category_id, node):
    if node is None:
        return None
    if node.category_id == category_id:
        return node
    left = find_category(category_id, node.left)
    if left:
        return left
    return find_category(category_id, node.right)

def find_path_to_root(category_id, node):
    target = find_category(category_id, node)
    path = []
    while target:
        path.append(target.name)
        target = target.parent
    return path

def lowest_common_ancestor(node, id1, id2):
    if node is None:
        return None
    if node.category_id == id1 or node.category_id == id2:
        return node
    left = lowest_common_ancestor(node.left, id1, id2)
    right = lowest_common_ancestor(node.right, id1, id2)
    if left and right:
        return node
    return left if left else right


# Testing
root = CategoryNode(1, "Technology", 100)
a = CategoryNode(2, "Programming", 50)
b = CategoryNode(3, "Design", 50)
c = CategoryNode(4, "Python", 30)
root.left = a
root.right = b
a.parent = root
b.parent = root
a.left = c
c.parent = a

print(calculate_height(root))
print(count_nodes(root))
print(count_leaves(root))
print(is_balanced(root))
print(is_full_binary_tree(root))
print(is_perfect_binary_tree(root))
print(is_complete_binary_tree(root))
print(find_category(4, root).name)
print(find_path_to_root(4, root))
print(lowest_common_ancestor(root, 4, 3).name)
empty = None
print(calculate_height(empty))
print(count_nodes(empty))
print(count_leaves(empty))
print(is_balanced(empty))
print(is_complete_binary_tree(empty))
single = CategoryNode(10, "Only", 1)
print(calculate_height(single))
print(count_nodes(single))
print(count_leaves(single))
print(is_full_binary_tree(single))
print(is_perfect_binary_tree(single))
skewed = CategoryNode(1, "A", 1)
skewed.left = CategoryNode(2, "B", 1)
skewed.left.left = CategoryNode(3, "C", 1)
print(calculate_height(skewed))
print(is_balanced(skewed))
print(is_complete_binary_tree(skewed))
not_full = CategoryNode(1, "Root", 1)
not_full.left = CategoryNode(2, "Child", 1)
print(is_full_binary_tree(not_full))
print(is_complete_binary_tree(not_full))