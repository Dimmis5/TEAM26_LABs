# LAB_05 - Basics of Tree Structures

## Team 26
**Team Members:**
- Kamilla VAISOVA - Exercise 2
- Diméo ZHANG - Exercise 1
- Yannick ZHANG - Exercise 3
---
## Exercise Descriptions

### Exercise 1: Graph Representations for Social Networks 

SocialGraph structure that models users as vertices and friendships as edges using two simultaneous internal representations: an Adjacency Matrix and an Adjacency Linked List. The system must support core operations such as adding or removing friendships, checking if two users are friends, retrieving a user's friend list, and calculating individual degrees. Beyond basic management, the exercise involves calculating global graph properties like completeness and edge density, while also providing functionality to convert data between the matrix and list formats.

### Exercise 2: Tree Traversals for Content Processing

The exercise focused on implementing classic binary tree traversals for a category hierarchy. In-order was used to display categories in sorted order, pre-order to export or serialize the tree, and post-order to aggregate metrics from children before processing parents. Additional analytics included finding the most popular category and the category with the most direct subcategories. A test script was included to run all traversals and print outputs, demonstrating practical applications like totals, leaf collection, and average depth.

### Exercise 3:  Generalized Trees (N-ary Trees) and Representations
This exercise focuses on the use of generalized trees (N-ary trees) to represent hierarchical category structures where each node can have multiple children. Recursive algorithms are implemented for tree traversals, height calculation, node and leaf counting, fan-out, and branching factor analysis. The exercise also explores the conversion between generalized trees and binary trees using the first child / next sibling representation, allowing the same hierarchy to be stored in different structural forms.

## Complexity Analysis Summary

Exercise, Time complexity, Space complexity
- Ex 1: Matrix O(1) for updates/checks and O(V^2) space; List O(d) for updates/checks and O(V+E) space
- Ex 2: O(n) for all traversals and analytics, space O(h) for recursion stack
- -Ex3 :The time complexity is O(n) for all traversals and metric calculations, as each node in the generalized tree is visited once. The conversion between generalized and binary trees also runs in O(n). The space complexity is O(d) for recursive methods, where d is the maximum tree depth, and O(n) for iterative breadth-first traversal using a queue.
- Ex 3: O(n), O(d)

