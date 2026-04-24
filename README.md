# LAB_07 - More Recursion

## Team 26
**Team Members:**
- Kamilla VAISOVA - Exercise 1
- Diméo ZHANG - Exercise 3
- Yannick ZHANG - Exercise 2
---
## Exercise Descriptions

### Exercise 1: Binary search trees
This is a Binary Search Tree (BST) that manages user profiles. Each node stores a user ID, name, and friends list. It supports inserting users, searching by ID, listing users in sorted order, deleting users, checking if the tree is balanced, and counting leaf nodes.

### Exercise 2:Binary Heap – Trending Posts Feed
In this exercise, we implemented a binary heap structure and its associated methods, and explored its application in a social network context. The heap organizes posts based on their number of likes, ensuring that the most popular content is always accessible at the root. 
By using operations such as insertion, update, and extraction, the structure maintains its efficiency through logarithmic time complexity. This makes it particularly well-suited for dynamic environments like social networks, where posts are constantly being updated and new content is frequently added.

This approach is highly efficient compared to a sorted array because it avoids the need to reorganize the entire dataset after each modification. Instead, it locally adjusts the structure using heapify operations, allowing fast updates and retrieval of trending posts. As a result, the binary heap provides an optimal solution for managing real-time ranking systems.

### Exercise 3: Prefix and Range Trees – Autocomplete & Activity Range Queries 
Trie structure to manage username autocomplete and a Segment Tree to analyze user activity range queries. In Part A, the Trie was built using nodes containing character dictionaries and user IDs to enable fast prefix searching and "search-as-you-type" suggestions for a database of 50,000 users. In Part B, the Segment Tree was constructed from an initial activity array to store daily post counts over a 30-day period. This structure allows the system to efficiently calculate total post sums, as well as identify minimum and maximum activity levels for any specific date range, such as rolling totals for a final week of activity

## Complexity Analysis Summary

Exercise, Time complexity, Space complexity
- ex 3: Autocomplete, O(L + S) for prefix search and result collection , O(N x L_{avg}) for total node storage








