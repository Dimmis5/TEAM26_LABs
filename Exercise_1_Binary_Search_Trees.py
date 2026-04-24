class UserBST:
    def __init__(self, user_id, name, friends):
        self.user_id = user_id
        self.name = name
        self.friends = friends
        self.left = None
        self.right = None


def insert(root, user_id, name, friends):
    if root is None:
        return UserBST(user_id, name, friends)
    if user_id < root.user_id:
        root.left = insert(root.left, user_id, name, friends)
    elif user_id > root.user_id:
        root.right = insert(root.right, user_id, name, friends)
    return root


def find(node, user_id):
    if node is None:
        return None
    if user_id == node.user_id:
        return node
    elif user_id < node.user_id:
        return find(node.left, user_id)
    else:
        return find(node.right, user_id)


def inorder(root, result_list):
    if root is not None:
        inorder(root.left, result_list)
        result_list.append(root.user_id)
        inorder(root.right, result_list)


def find_min(node):
    if node.left is None:
        return node
    return find_min(node.left)


def delete(root, user_id):
    if root is None:
        return None
    if user_id < root.user_id:
        root.left = delete(root.left, user_id)
    elif user_id > root.user_id:
        root.right = delete(root.right, user_id)
    else:
        if root.right is None and root.left is None:
            return None
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        successor = find_min(root.right)
        root.user_id = successor.user_id
        root.name = successor.name
        root.friends = successor.friends
        root.right = delete(root.right, successor.user_id)
    return root


def get_height(node):
    if node is None:
        return 0
    left_h = get_height(node.left)
    right_h = get_height(node.right)
    return 1 + max(left_h, right_h)


def is_balanced(node):
    if node is None:
        return True
    left_h = get_height(node.left)
    right_h = get_height(node.right)
    if abs(left_h - right_h) > 1:
        return False
    return is_balanced(node.left) and is_balanced(node.right)


def get_leaf_count(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return get_leaf_count(node.left) + get_leaf_count(node.right)


def suggest_friends(root, user_id, max_suggestions=5):
    user = find(root, user_id)
    if user is None:
        return []
    direct_friends = set(user.friends)
    fof_count = {}
    for fid in direct_friends:
        friend_node = find(root, fid)
        if friend_node is not None:
            for fof_id in friend_node.friends:
                if fof_id != user_id and fof_id not in direct_friends:
                    fof_count[fof_id] = fof_count.get(fof_id, 0) + 1
    sorted_fof = sorted(fof_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_fof[:max_suggestions]


root = None
root = insert(root, 10, "Alice",   [20, 30])
root = insert(root, 20, "Bob",     [10, 30, 40, 50])
root = insert(root, 30, "Charlie", [10, 20, 60])
root = insert(root, 40, "Diana",   [20, 60, 70])
root = insert(root, 50, "Eve",     [20, 60])
root = insert(root, 60, "Frank",   [30, 40, 50])
root = insert(root, 70, "Grace",   [40])
root = insert(root,  5, "Hank",    [10])

print("=== INORDER TRAVERSAL ===")
result = []
inorder(root, result)
print("Sorted user IDs:", result)

print("\n=== FIND ===")
node = find(root, 30)
print(f"Found user 30: {node.name}, friends={node.friends}")
print("Find user 99:", find(root, 99))

print("\n=== SUGGEST FRIENDS ===")
print("Suggestions for Alice (10):", suggest_friends(root, 10))
print("Suggestions for Bob   (20):", suggest_friends(root, 20))
print("Suggestions for Diana (40):", suggest_friends(root, 40))

print("\n=== ANALYTICS ===")
print("Height:", get_height(root))
print("Balanced:", is_balanced(root))
print("Leaf count:", get_leaf_count(root))

print("\n=== DELETE ===")
print("Deleting user 20 (Bob, two children)...")
root = delete(root, 20)
result2 = []
inorder(root, result2)
print("Inorder after delete:", result2)
print("Find user 20 after delete:", find(root, 20))

print("\nDeleting user 5 (Hank, leaf)...")
root = delete(root, 5)
result3 = []
inorder(root, result3)
print("Inorder after delete:", result3)

print("\nHeight after deletions:", get_height(root))
print("Balanced after deletions:", is_balanced(root))
print("Leaf count after deletions:", get_leaf_count(root))