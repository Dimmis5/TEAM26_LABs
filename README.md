# LAB_07 - More Recursion

## Team 26
**Team Members:**
- Kamilla VAISOVA - Exercise 
- Diméo ZHANG - Exercise 2
- Yannick ZHANG - Exercise  3
---
## Exercise Descriptions

### Exercise 1: Influencer Coverage – Minimal User Set (Ref. Vertex Cover variant)
Influencer Coverage problem by first creating an `is_valid_coverage` function to verify if every user in the social network is either selected or directly connected to a selected node. I then implemented two search strategies: a brute-force method using bitmasking to find the exact minimum dominating set for small graphs and a greedy approximation that efficiently picks users based on the number of new nodes they cover. Finally, I integrated these functions into a complete Python script with a test environment, demonstrating how the greedy heuristic provides a fast alternative to the computationally expensive exact search used for finding optimal influence.

### Exercise 2: Viral Message Timing – Maximize Total Reach (Ref. 0/1 Knapsack)
The core objective is to select a specific subset of users to target with a promotional message in order to maximize the total audience influence (reach). This selection is strictly bounded by a financial constraint: each user has an individual server cost, and the total cost of all chosen users cannot exceed a fixed available budget. The assignment requires solving this problem using two different strategies: an exact dynamic programming method that guarantees finding the absolute best possible combination of users , and a fast ratio-based greedy heuristic that prioritizes users with the highest reach-to-cost efficiency but may settle for a sub-optimal solution in certain scenarios

### Exercise 3: Group Formation – Minimize External Friends (Ref. Balanced Minimum Cut)
In this exercise, we studied the problem of splitting users into two balanced groups while minimizing the number of friendships between the groups. The graph is represented with users as nodes and friendships as undirected edges. First, we implemented a function to count the number of cross edges between two groups. Then, we used a greedy algorithm that starts from a random balanced split and tries to improve it by moving one user at a time, only if the move reduces the number of cross edges. Finally, we improved this approach with local search by running the greedy algorithm several times with different random initial splits and keeping the best solution found. This method does not guarantee the optimal solution, but it gives a reasonable result faster than testing all possible partitions.

## Complexity Analysis Summary

Exercise, Time complexity, Space complexity
- ex 1: Influencer Coverage, O(2^N x (N + E)) for exact search and O(N x (N + E)) for greedy approximation , O(N + E) for adjacency list storage and coverage tracking.
- ex 2: Viral Message Timing, O(N x budget) for exact dynamic programming and O(N log N) for ratio-based greedy approximation, O(N x budget) for DP table storage and backtracking.
 -ex 3: - ex 3: Balanced Group Formation, O(E) for cross-edge counting, O(P × N × (N + E)) for the greedy algorithm, and O(I × greedy) for local search, O(N + E) for adjacency list storage and group tracking,where N=number of users,E=number of friendships,P=number of greedy improvement rounds,I=number of local search iterations,greedy=complexity of one greedy run








