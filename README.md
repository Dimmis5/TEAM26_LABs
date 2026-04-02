# LAB_05 - Basics of Tree Structures

## Team 26
**Team Members:**
- Kamilla VAISOVA - Exercise 1 / 3
- Diméo ZHANG - Exercise 2
- Yannick ZHANG - Exercise 2 / 1
---
## Exercise Descriptions

### Exercise 1:
We implemented a recursive system to manage nested comment threads using a CommentNode structure. Each comment contains its id, user, content, likes, and a list of replies.

We created recursive functions to display the thread with indentation, count total comments, sum all likes, and find the deepest reply level. We also added search functions to find comments by user and detect keywords, as well as a deletion function that removes a comment and all its replies.

This exercise shows that recursion is well suited for hierarchical data like comment threads, as each reply can be processed in the same way as the main comment. 
### Exercise 2: Tree Traversals for Content Processing

The exercise focused on implementing classic binary tree traversals for a category hierarchy. In-order was used to display categories in sorted order, pre-order to export or serialize the tree, and post-order to aggregate metrics from children before processing parents. Additional analytics included finding the most popular category and the category with the most direct subcategories. A test script was included to run all traversals and print outputs, demonstrating practical applications like totals, leaf collection, and average depth.

### Exercise 3:  Recursion to Iteration
This exercise explores the use of recursion and its iterative equivalent for processing nested comment threads. A recursive approach is used to flatten a comment tree in depth-first order, demonstrating how naturally recursion handles hierarchical data structures. The same functionality is then implemented iteratively using an explicit stack, simulating the call stack to avoid recursion depth limitations.

Additionally, the exercise introduces tail recursion for counting comments and its conversion into a loop-based solution. This highlights the trade-offs between readability and control over memory usage, especially in systems where deep nesting may cause stack overflow.

## Complexity Analysis Summary

Exercise, Time complexity, Space complexity
- Ex 1: O(n) for display, count, total likes, search, and deletion since each comment is visited once, O(n) also for finding deepest reply, space O(d) for recursion stack where d is the maximum nesting depth of the thread.
- Ex 2: O(n) for all traversals and analytics, space O(h) for recursion stack
- Ex 3: O(n), O(d)

