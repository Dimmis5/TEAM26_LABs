# LAB_07 - More Recursion

## Team 26
**Team Members:**
- Kamilla VAISOVA - Exercise 1
- Diméo ZHANG - Exercise 1
- Yannick ZHANG - Exercise 2
---
## Exercise Descriptions

### Exercise 1: Influencer Coverage – Minimal User Set (Ref. Vertex Cover variant)
Influencer Coverage problem by first creating an `is_valid_coverage` function to verify if every user in the social network is either selected or directly connected to a selected node. I then implemented two search strategies: a brute-force method using bitmasking to find the exact minimum dominating set for small graphs and a greedy approximation that efficiently picks users based on the number of new nodes they cover. Finally, I integrated these functions into a complete Python script with a test environment, demonstrating how the greedy heuristic provides a fast alternative to the computationally expensive exact search used for finding optimal influence.

### Exercise 2:Binary Heap – Trending Posts Feed
In this exercise, we implemented a binary heap structure and its associated methods, and explored its application in a social network context. The heap organizes posts based on their number of likes, ensuring that the most popular content is always accessible at the root. 
By using operations such as insertion, update, and extraction, the structure maintains its efficiency through logarithmic time complexity. This makes it particularly well-suited for dynamic environments like social networks, where posts are constantly being updated and new content is frequently added.

This approach is highly efficient compared to a sorted array because it avoids the need to reorganize the entire dataset after each modification. Instead, it locally adjusts the structure using heapify operations, allowing fast updates and retrieval of trending posts. As a result, the binary heap provides an optimal solution for managing real-time ranking systems.

### Exercise 3: Prefix and Range Trees – Autocomplete & Activity Range Queries 
Trie structure to manage username autocomplete and a Segment Tree to analyze user activity range queries. In Part A, the Trie was built using nodes containing character dictionaries and user IDs to enable fast prefix searching and "search-as-you-type" suggestions for a database of 50,000 users. In Part B, the Segment Tree was constructed from an initial activity array to store daily post counts over a 30-day period. This structure allows the system to efficiently calculate total post sums, as well as identify minimum and maximum activity levels for any specific date range, such as rolling totals for a final week of activity

## Complexity Analysis Summary

Exercise, Time complexity, Space complexity
- ex 1: Influencer Coverage, O(2^N x (N + E)) for exact search and O(N x (N + E)) for greedy approximation , O(N + E) for adjacency list storage and coverage tracking.
- ex 3: Autocomplete, O(L + S) for prefix search and result collection , O(N x L_{avg}) for total node storage








