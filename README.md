# LAB_05 - Basics of Tree Structures

## Team 26
**Team Members:**
- Kamilla VAISOVA - Exercise 1 
- Diméo ZHANG - Exercise 2
- Yannick ZHANG - Exercise 3
---
## Exercise Descriptions

### Exercise 1: Binary trees 
This exercise represents social media categories using a binary tree, where each node is a category and its children are subcategories. To solve it, we created a CategoryNode class and used mainly recursion to traverse the tree and compute values like height, number of nodes, and balance. Each function works by solving the problem on the left and right subtrees. For checking if the tree is complete, we used a queue with level-order traversal (BFS). Overall, the solution is based on efficiently traversing the tree and breaking problems into smaller recursive steps.

### Exercise 2: Tree Traversals for Content Processing

The exercise focused on implementing classic binary tree traversals for a category hierarchy. In-order was used to display categories in sorted order, pre-order to export or serialize the tree, and post-order to aggregate metrics from children before processing parents. Additional analytics included finding the most popular category and the category with the most direct subcategories. A test script was included to run all traversals and print outputs, demonstrating practical applications like totals, leaf collection, and average depth.

### Exercise 3:  Generalized Trees (N-ary Trees) and Representations
This exercise focuses on the use of generalized trees (N-ary trees) to represent hierarchical category structures where each node can have multiple children. Recursive algorithms are implemented for tree traversals, height calculation, node and leaf counting, fan-out, and branching factor analysis. The exercise also explores the conversion between generalized trees and binary trees using the first child / next sibling representation, allowing the same hierarchy to be stored in different structural forms.

## Complexity Analysis Summary

Exercise, Time complexity, Space complexity
- Ex 1: time: tree traversal, height, count, search, complete tree O(n), balanced check O(n^2); space: O(n)
- Ex 2: O(n) for all traversals and analytics, space O(h) for recursion stack
- -Ex3 :The time complexity is O(n) for all traversals and metric calculations, as each node in the generalized tree is visited once. The conversion between generalized and binary trees also runs in O(n). The space complexity is O(d) for recursive methods, where d is the maximum tree depth, and O(n) for iterative breadth-first traversal using a queue.
- Ex 3: O(n), O(d)

