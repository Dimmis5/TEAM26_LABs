# LAB_06 - Basics of Graph Structures

## Team 26
**Team Members:**
- Kamilla VAISOVA - Exercise 2
- Diméo ZHANG - Exercise 1
- Yannick ZHANG - Exercise 3
---
## Exercise Descriptions

### Exercise 1: Graph Representations for Social Networks 

SocialGraph structure that models users as vertices and friendships as edges using two simultaneous internal representations: an Adjacency Matrix and an Adjacency Linked List. The system must support core operations such as adding or removing friendships, checking if two users are friends, retrieving a user's friend list, and calculating individual degrees. Beyond basic management, the exercise involves calculating global graph properties like completeness and edge density, while also providing functionality to convert data between the matrix and list formats.

### Exercise 2: Graph Traversals

This exercise works on a graph of users, like a social network, where users are nodes and friendships are edges. It implements Depth-First Search (DFS) (recursive & iterative), connected components detection (groups of users connected together), graph connectivity check, path existence between two users, component size analysis, isolation detection (users with no connections). Overall, it analyzes how users are connected in a network and extracts structural information about that network.

### Exercise 3:  
This exercise focuses on a social network graph where each user is represented as a node and each friendship as an edge. It uses Breadth-First Search (BFS) to explore connections level by level, making it possible to find the shortest path between users, measure degrees of separation, and identify users within a given number of hops. It also provides network analysis features such as distance distribution, average separation, and friend recommendations based on indirect connections.

## Complexity Analysis Summary

Exercise, Time complexity, Space complexity
- Ex 1: Matrix O(1) for updates/checks and O(V^2) space; List O(d) for updates/checks and O(V+E) space
- Ex 2: Time : O(V+E), space: O(V)
- Ex3 :Most of the function the time complexity is O(V+E) and the space compexiy is O(V). 

