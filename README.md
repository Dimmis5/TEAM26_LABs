# LAB_07 - More Recursion

## Team 26
**Team Members:**
- Kamilla VAISOVA - Exercise 
- Diméo ZHANG - Exercise 3
- Yannick ZHANG - Exercise 2
---
## Exercise Descriptions

### Exercise 1: Divide & Conquer – Spatial Splitting
Recursive Quadtree decomposition that divides a 2D space into four equal quadrants until a minimum size is reached, effectively partitioning the area into a hierarchical grid. By integrating a point-counting function, the algorithm calculates the density of each region—the ratio of points to area—and recursively filters the space to return only those segments exceeding a specific threshold. This Divide and Conquer approach is highly efficient for identifying data clusters because it allows the program to "prune" or ignore vast empty areas while focusing computational resources on densely populated "hotspots," significantly optimizing the search process compared to a standard linear scan.

### Exercise 2:Binary Heap – Trending Posts Feed
In this exercise, we implemented a binary heap structure and its associated methods, and explored its application in a social network context. The heap organizes posts based on their number of likes, ensuring that the most popular content is always accessible at the root. 
By using operations such as insertion, update, and extraction, the structure maintains its efficiency through logarithmic time complexity. This makes it particularly well-suited for dynamic environments like social networks, where posts are constantly being updated and new content is frequently added.

This approach is highly efficient compared to a sorted array because it avoids the need to reorganize the entire dataset after each modification. Instead, it locally adjusts the structure using heapify operations, allowing fast updates and retrieval of trending posts. As a result, the binary heap provides an optimal solution for managing real-time ranking systems.

### Exercise 3: Prefix and Range Trees – Autocomplete & Activity Range Queries 
Trie structure to manage username autocomplete and a Segment Tree to analyze user activity range queries. In Part A, the Trie was built using nodes containing character dictionaries and user IDs to enable fast prefix searching and "search-as-you-type" suggestions for a database of 50,000 users. In Part B, the Segment Tree was constructed from an initial activity array to store daily post counts over a 30-day period. This structure allows the system to efficiently calculate total post sums, as well as identify minimum and maximum activity levels for any specific date range, such as rolling totals for a final week of activity

## Complexity Analysis Summary

Exercise, Time complexity, Space complexity
- ex 1: spatial splitting, $O(N log(S/min_size))$, $O(log(S/min_size))
- ex 2: sierpinski, O(3^depth), O(depth) ; tree, O(2^depth), O(depth) ; fractal dimension, O(B × N²/s²), O(N²)
- ex 3: Autocomplete, O(L + S) for prefix search and result collection , O(N x L_{avg}) for total node storage








