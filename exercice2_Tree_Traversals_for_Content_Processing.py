class CategoryNode:
    def __init__(self, category_id, name, post_count):
        self.category_id = category_id
        self.name = name
        self.post_count = post_count
        self.left = None
        self.right = None
        self.parent = None

# Part A: In-order Traversal
def in_order_collect(node):
    if node is None:
        return []
    return in_order_collect(node.left) + [node.name] + in_order_collect(node.right)

def in_order_accumulate_posts(node):
    if node is None:
        return 0
    left_sum = in_order_accumulate_posts(node.left)
    right_sum = in_order_accumulate_posts(node.right)
    total = left_sum + right_sum + node.post_count
    return total

def in_order_find_kth(node, k):
    if node is None:
        return (None, 0)
    
    left_result, left_count = in_order_find_kth(node.left, k)
    if left_result is not None:
        return (left_result, left_count)
    
    if left_count + 1 == k:
        return (node.name, left_count + 1)
    
    right_result, right_count = in_order_find_kth(node.right, k - (left_count + 1))
    if right_result is not None:
        return (right_result, left_count + 1 + right_count)
    
    return (None, left_count + 1 + right_count)

# Part B: Pre-order Traversal

def pre_order_export(node):
    if node is None:
        return ""
    result = f"{node.name}({node.post_count})\n"
    result += pre_order_export(node.left)
    result += pre_order_export(node.right)
    return result

def pre_order_copy(node):
    if node is None:
        return None
    new_node = CategoryNode(node.category_id, node.name, node.post_count)
    new_node.left = pre_order_copy(node.left)
    new_node.right = pre_order_copy(node.right)
    if new_node.left:
        new_node.left.parent = new_node
    if new_node.right:
        new_node.right.parent = new_node
    return new_node

def pre_order_serialize(node):
    if node is None:
        return ""
    result = f"{node.name}({node.post_count})"
    left_part = pre_order_serialize(node.left)
    right_part = pre_order_serialize(node.right)
    if left_part:
        result += "|" + left_part
    if right_part:
        result += "|" + right_part
    return result

# Part C: Post-order Traversal

def post_order_total_posts(node):
    if node is None:
        return 0
    left_sum = post_order_total_posts(node.left)
    right_sum = post_order_total_posts(node.right)
    total = left_sum + right_sum + node.post_count
    return total

def post_order_average_depth(node):
    if node is None:
        return (0, 0)  
    if node.left is None and node.right is None:
        return (0, 1)
    left_sum, left_count = post_order_average_depth(node.left)
    right_sum, right_count = post_order_average_depth(node.right)
    total_sum = left_sum + right_sum + left_count + right_count
    total_count = left_count + right_count
    return (total_sum, total_count)

def post_order_collect_leaves(node):
    if node is None:
        return []
    left_leaves = post_order_collect_leaves(node.left)
    right_leaves = post_order_collect_leaves(node.right)
    if node.left is None and node.right is None:
        return [node.name]
    return left_leaves + right_leaves

# Analytics

def find_most_popular_category(node):
    if node is None:
        return None
    left_best = find_most_popular_category(node.left)
    right_best = find_most_popular_category(node.right)
    best = node
    if left_best and left_best.post_count > best.post_count:
        best = left_best
    if right_best and right_best.post_count > best.post_count:
        best = right_best
    return best

def category_with_most_subcategories(node):
    if node is None:
        return None
    left_best = category_with_most_subcategories(node.left)
    right_best = category_with_most_subcategories(node.right)
    current_children = (1 if node.left else 0) + (1 if node.right else 0)
    best = node
    best_children = current_children
    if left_best:
        left_children = (1 if left_best.left else 0) + (1 if left_best.right else 0)
        if left_children > best_children:
            best = left_best
            best_children = left_children
    if right_best:
        right_children = (1 if right_best.left else 0) + (1 if right_best.right else 0)
        if right_children > best_children:
            best = right_best
    return best


#Test 

root = CategoryNode(1, "Technology", 150)
root.left = CategoryNode(2, "Programming", 85)
root.right = CategoryNode(3, "Design", 65)
root.left.left = CategoryNode(4, "Python", 42)
root.left.right = CategoryNode(5, "Java", 30)
root.left.left.left = CategoryNode(6, "Django", 18)
root.left.left.right = CategoryNode(7, "Flask", 12)
root.right.left = CategoryNode(8, "UI/UX", 38)
root.right.right = CategoryNode(9, "Graphics", 22)


print("In-order Traversal")
in_order_names = in_order_collect(root)
print(" → ".join(in_order_names))

print("\nIn-order Accumulate Posts ")
total_posts = in_order_accumulate_posts(root)
print("Total posts (all categories):", total_posts)

print("\nIn-order Find k-th")
k = 4
kth_name, _ = in_order_find_kth(root, k)
print(f"{k}-th category in in-order:", kth_name)

print("\nPre-order Export")
print(pre_order_export(root))

print("Pre-order Copy & Serialize")
copy_root = pre_order_copy(root)
serialized = pre_order_serialize(copy_root)
print("Serialized:", serialized)

print("\nPost-order Total Posts") 
post_total = post_order_total_posts(root)
print("Total posts in all categories:", post_total)

print("\nPost-order Average Depth of Leaves ")
sum_depth, leaf_count = post_order_average_depth(root)
average_depth = sum_depth / leaf_count if leaf_count else 0
print("Average depth of leaves:", average_depth)

print("\nPost-order Collect Leaves ")
leaves = post_order_collect_leaves(root)
print("Leaves:", leaves)

print("\nAnalytics ")
most_popular = find_most_popular_category(root)
print(f"Most popular category: {most_popular.name} ({most_popular.post_count} posts)")

most_subcategories = category_with_most_subcategories(root)
children_count = (1 if most_subcategories.left else 0) + (1 if most_subcategories.right else 0)
print(f"Category with most direct subcategories: {most_subcategories.name} ({children_count} children)")


