import random

#Part A: Autocomplete Trie

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_username = False 
        self.user_id = None 

class AutocompleteTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, username, user_id):
        node = self.root
        for char in username.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_username = True
        node.user_id = user_id

    def search(self, username):
        node = self._navigate_to(username)
        if node and node.is_end_of_username:
            return node.user_id
        return None

    def starts_with(self, prefix):
        return self._navigate_to(prefix) is not None

    def autocomplete(self, prefix, max_results=10):
        node = self._navigate_to(prefix)
        if not node:
            return []
        
        results = []
        self._dfs_collect(node, prefix.lower(), results, max_results)
        return results

    def _navigate_to(self, text):
        node = self.root
        for char in text.lower():
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def _dfs_collect(self, node, current_path, results, max_res):
        if len(results) >= max_res:
            return
        
        if node.is_end_of_username:
            results.append((current_path, node.user_id))
            
        for char, next_node in sorted(node.children.items()):
            self._dfs_collect(next_node, current_path + char, results, max_res)

    
    def count_words(self):
        return self._count_recursive(self.root)

    def _count_recursive(self, node):
        count = 1 if node.is_end_of_username else 0
        for child in node.children.values():
            count += self._count_recursive(child)
        return count

    def get_height(self):
        return self._get_height_recursive(self.root)

    def _get_height_recursive(self, node):
        if not node.children:
            return 0
        return 1 + max(self._get_height_recursive(c) for c in node.children.values())
    
#Part B: Activity Segment Tree


class ActivitySegmentTree:
    def __init__(self, activity_array):
        self.n = len(activity_array) 
        self.tree = [0] * (4 * self.n)
        self.max_tree = [-float('inf')] * (4 * self.n)
        self.min_tree = [float('inf')] * (4 * self.n)
        self._build(activity_array, 0, 0, self.n - 1)

    def _build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
            self.max_tree[node] = arr[start]
            self.min_tree[node] = arr[start]
            return

        mid = (start + end) // 2
        self._build(arr, 2 * node + 1, start, mid)
        self._build(arr, 2 * node + 2, mid + 1, end)
        
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
        self.max_tree[node] = max(self.max_tree[2 * node + 1], self.max_tree[2 * node + 2])
        self.min_tree[node] = min(self.min_tree[2 * node + 1], self.min_tree[2 * node + 2])

    def query(self, l, r):
        return self._query_sum(0, 0, self.n - 1, l, r)

    def _query_sum(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        return self._query_sum(2 * node + 1, start, mid, l, r) + \
               self._query_sum(2 * node + 2, mid + 1, end, l, r)

    def get_range_max(self, l, r):
        return self._query_generic(self.max_tree, max, -float('inf'), 0, 0, self.n - 1, l, r)

    def get_range_min(self, l, r):
        return self._query_generic(self.min_tree, min, float('inf'), 0, 0, self.n - 1, l, r)

    def _query_generic(self, target_tree, func, identity, node, start, end, l, r):
        if r < start or end < l:
            return identity
        if l <= start and end <= r:
            return target_tree[node]
        mid = (start + end) // 2
        return func(self._query_generic(target_tree, func, identity, 2 * node + 1, start, mid, l, r),
                    self._query_generic(target_tree, func, identity, 2 * node + 2, mid + 1, end, l, r))


    def get_tree_size(self):
        return len(self.tree)

    def get_leaf_values(self):
        leaves = []
        self._collect_leaves(0, 0, self.n - 1, leaves)
        return leaves

    def _collect_leaves(self, node, start, end, leaves):
        if start == end:
            leaves.append(self.tree[node])
            return
        mid = (start + end) // 2
        self._collect_leaves(2 * node + 1, start, mid, leaves)
        self._collect_leaves(2 * node + 2, mid + 1, end, leaves)

#Test


trie = AutocompleteTrie()
for i in range(50000):
    trie.insert(f"user_{i}", i)
print(f"Autocomplete pour 'user_10': {trie.autocomplete('user_10')}")

activity = [random.randint(0, 1000) for _ in range(30)]
stree = ActivitySegmentTree(activity)
print(f"Total posts last week: {stree.query(23, 29)}")