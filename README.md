# LAB_07 - More Recursion

## Team 26
**Team Members:**
- Kamilla VAISOVA - Exercise 
- Diméo ZHANG - Exercise 2
- Yannick ZHANG - Exercise 
---
## Exercise Descriptions

### Exercise 1: Influencer Coverage – Minimal User Set (Ref. Vertex Cover variant)
Influencer Coverage problem by first creating an `is_valid_coverage` function to verify if every user in the social network is either selected or directly connected to a selected node. I then implemented two search strategies: a brute-force method using bitmasking to find the exact minimum dominating set for small graphs and a greedy approximation that efficiently picks users based on the number of new nodes they cover. Finally, I integrated these functions into a complete Python script with a test environment, demonstrating how the greedy heuristic provides a fast alternative to the computationally expensive exact search used for finding optimal influence.

### Exercise 2: Viral Message Timing – Maximize Total Reach (Ref. 0/1 Knapsack)
The core objective is to select a specific subset of users to target with a promotional message in order to maximize the total audience influence (reach). This selection is strictly bounded by a financial constraint: each user has an individual server cost, and the total cost of all chosen users cannot exceed a fixed available budget. The assignment requires solving this problem using two different strategies: an exact dynamic programming method that guarantees finding the absolute best possible combination of users , and a fast ratio-based greedy heuristic that prioritizes users with the highest reach-to-cost efficiency but may settle for a sub-optimal solution in certain scenarios

### Exercise 3: Prefix and Range Trees – Autocomplete & Activity Range Queries 
Trie structure to manage username autocomplete and a Segment Tree to analyze user activity range queries. In Part A, the Trie was built using nodes containing character dictionaries and user IDs to enable fast prefix searching and "search-as-you-type" suggestions for a database of 50,000 users. In Part B, the Segment Tree was constructed from an initial activity array to store daily post counts over a 30-day period. This structure allows the system to efficiently calculate total post sums, as well as identify minimum and maximum activity levels for any specific date range, such as rolling totals for a final week of activity

## Complexity Analysis Summary

Exercise, Time complexity, Space complexity
- ex 1: Influencer Coverage, O(2^N x (N + E)) for exact search and O(N x (N + E)) for greedy approximation , O(N + E) for adjacency list storage and coverage tracking.
- ex 2: Viral Message Timing, O(N x budget) for exact dynamic programming and O(N log N) for ratio-based greedy approximation, O(N x budget) for DP table storage and backtracking.
- ex 3: Autocomplete, O(L + S) for prefix search and result collection , O(N x L_{avg}) for total node storage








