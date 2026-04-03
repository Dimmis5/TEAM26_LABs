from collections import deque
from typing import List, Optional


class GeneralizedCategoryNode:
    def __init__(
        self,
        category_id=None,
        name: str = "",
        post_count: int = 0,
        children: Optional[List["GeneralizedCategoryNode"]] = None,
        parent: Optional["GeneralizedCategoryNode"] = None,
    ):
        self.category_id = category_id
        self.name = name
        self.post_count = post_count
        self.children = children if children is not None else []
        self.parent = parent


class BinaryCategoryNode:
    def __init__(
        self,
        category_id=None,
        name: str = "",
        post_count: int = 0,
        left: Optional["BinaryCategoryNode"] = None,
        right: Optional["BinaryCategoryNode"] = None,
        parent: Optional["BinaryCategoryNode"] = None,
    ):
        self.category_id = category_id
        self.name = name
        self.post_count = post_count
        self.left = left
        self.right = right
        self.parent = parent


def generalized_to_binary(gen_root: Optional[GeneralizedCategoryNode]) -> Optional[BinaryCategoryNode]:
    if gen_root is None:
        return None

    new_binary_node = BinaryCategoryNode(
        category_id=gen_root.category_id,
        name=gen_root.name,
        post_count=gen_root.post_count,
    )

    if len(gen_root.children) == 0:
        return new_binary_node

    first_child = gen_root.children[0]
    new_binary_node.left = generalized_to_binary(first_child)

    if new_binary_node.left is not None:
        new_binary_node.left.parent = new_binary_node

    current_sibling = new_binary_node.left

    for i in range(1, len(gen_root.children)):
        next_child = gen_root.children[i]
        current_sibling.right = generalized_to_binary(next_child)

        if current_sibling.right is not None:
            current_sibling.right.parent = new_binary_node

        current_sibling = current_sibling.right

    return new_binary_node


def binary_to_generalized(bin_root: Optional[BinaryCategoryNode]) -> Optional[GeneralizedCategoryNode]:
    if bin_root is None:
        return None

    gen = GeneralizedCategoryNode(
        category_id=bin_root.category_id,
        name=bin_root.name,
        post_count=bin_root.post_count,
    )

    current_child = bin_root.left

    while current_child is not None:
        val = binary_to_generalized(current_child)
        if val is not None:
            val.parent = gen
            gen.children.append(val)
        current_child = current_child.right

    return gen


def pre_order_generalized(node: Optional[GeneralizedCategoryNode]) -> List[str]:
    if node is None:
        return []

    result = [node.name]

    for i in range(len(node.children)):
        result.extend(pre_order_generalized(node.children[i]))

    return result


def post_order_generalized(node: Optional[GeneralizedCategoryNode]) -> List[str]:
    if node is None:
        return []

    result = []

    for i in range(len(node.children)):
        result.extend(post_order_generalized(node.children[i]))

    result.append(node.name)
    return result


def level_order_generalized(node: Optional[GeneralizedCategoryNode]) -> List[str]:
    if node is None:
        return []

    que = deque([node])
    result = []

    while que:
        val = que.popleft()
        result.append(val.name)

        for i in range(len(val.children)):
            que.append(val.children[i])

    return result


def calculate_fan_out(node: Optional[GeneralizedCategoryNode]) -> int:
    if node is None:
        return 0

    max_val = len(node.children)

    for i in range(len(node.children)):
        val = calculate_fan_out(node.children[i])
        if val > max_val:
            max_val = val

    return max_val


def calculate_height_generalized(node: Optional[GeneralizedCategoryNode]) -> int:
    if node is None:
        return 0

    if len(node.children) == 0:
        return 1

    max_height = 0

    for i in range(len(node.children)):
        child = node.children[i]
        child_height = calculate_height_generalized(child)

        if child_height > max_height:
            max_height = child_height

    return max_height + 1


def count_nodes_generalized(node: Optional[GeneralizedCategoryNode]) -> int:
    if node is None:
        return 0

    count = 1

    for i in range(len(node.children)):
        count += count_nodes_generalized(node.children[i])

    return count


def count_leaves_generalized(node: Optional[GeneralizedCategoryNode]) -> int:
    if node is None:
        return 0

    if len(node.children) == 0:
        return 1

    count = 0

    for i in range(len(node.children)):
        count += count_leaves_generalized(node.children[i])

    return count


def calculate_branching_factor(node: Optional[GeneralizedCategoryNode]) -> float:
    if node is None:
        return 0.0

    que = deque([node])
    total_children = 0
    non_leaf_nodes = 0

    while que:
        val = que.popleft()

        if len(val.children) > 0:
            total_children += len(val.children)
            non_leaf_nodes += 1

        for i in range(len(val.children)):
            que.append(val.children[i])

    if non_leaf_nodes == 0:
        return 0.0

    return total_children / non_leaf_nodes


def pre_order_binary(node: Optional[BinaryCategoryNode]) -> List[str]:
    if node is None:
        return []

    result = [node.name]
    result.extend(pre_order_binary(node.left))
    result.extend(pre_order_binary(node.right))
    return result


def print_generalized_tree(node: Optional[GeneralizedCategoryNode], level: int = 0) -> None:
    if node is None:
        return

    print("  " * level + f"- {node.name} ({node.post_count})")
    for child in node.children:
        print_generalized_tree(child, level + 1)


def print_binary_tree(node: Optional[BinaryCategoryNode], level: int = 0, label: str = "Root") -> None:
    if node is None:
        return

    print("  " * level + f"{label}: {node.name} ({node.post_count})")
    print_binary_tree(node.left, level + 1, "L")
    print_binary_tree(node.right, level + 1, "R")


def build_test_tree() -> GeneralizedCategoryNode:
    technology = GeneralizedCategoryNode(1, "Technology", 150)
    programming = GeneralizedCategoryNode(2, "Programming", 85)
    design = GeneralizedCategoryNode(3, "Design", 65)
    business = GeneralizedCategoryNode(4, "Business", 90)
    python_node = GeneralizedCategoryNode(5, "Python", 42)
    java = GeneralizedCategoryNode(6, "Java", 30)
    uiux = GeneralizedCategoryNode(7, "UI/UX", 38)
    graphics = GeneralizedCategoryNode(8, "Graphics", 22)
    finance = GeneralizedCategoryNode(9, "Finance", 40)
    marketing = GeneralizedCategoryNode(10, "Marketing", 35)
    hr = GeneralizedCategoryNode(11, "HR", 20)
    django = GeneralizedCategoryNode(12, "Django", 18)
    flask = GeneralizedCategoryNode(13, "Flask", 12)

    technology.children = [programming, design, business]
    programming.parent = technology
    design.parent = technology
    business.parent = technology

    programming.children = [python_node, java]
    python_node.parent = programming
    java.parent = programming

    design.children = [uiux, graphics]
    uiux.parent = design
    graphics.parent = design

    business.children = [finance, marketing, hr]
    finance.parent = business
    marketing.parent = business
    hr.parent = business

    python_node.children = [django, flask]
    django.parent = python_node
    flask.parent = python_node

    return technology


if __name__ == "__main__":
    gen_root = build_test_tree()

    print("GENERALIZED TREE")
    print_generalized_tree(gen_root)
    print()

    print("PRE-ORDER GENERALIZED")
    print(pre_order_generalized(gen_root))
    print()

    print("POST-ORDER GENERALIZED")
    print(post_order_generalized(gen_root))
    print()

    print("LEVEL-ORDER GENERALIZED")
    print(level_order_generalized(gen_root))
    print()

    print("FAN-OUT")
    print(calculate_fan_out(gen_root))
    print()

    print("HEIGHT")
    print(calculate_height_generalized(gen_root))
    print()

    print("COUNT NODES")
    print(count_nodes_generalized(gen_root))
    print()

    print("COUNT LEAVES")
    print(count_leaves_generalized(gen_root))
    print()

    print("BRANCHING FACTOR")
    print(calculate_branching_factor(gen_root))
    print()

    bin_root = generalized_to_binary(gen_root)

    print("BINARY TREE (FIRST CHILD / NEXT SIBLING)")
    print_binary_tree(bin_root)
    print()

    print("PRE-ORDER BINARY")
    print(pre_order_binary(bin_root))
    print()

    converted_back = binary_to_generalized(bin_root)

    print("GENERALIZED TREE AFTER CONVERSION BACK")
    print_generalized_tree(converted_back)
    print()

    print("PRE-ORDER AFTER CONVERSION BACK")
    print(pre_order_generalized(converted_back))
    print()