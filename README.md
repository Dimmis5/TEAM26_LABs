# LAB_05 - Basics of Tree Structures

## Team 26
**Team Members:**
- Kamilla VAISOVA - Exercise 1 / 3
- Diméo ZHANG - Exercise 2
- Yannick ZHANG - Exercise 3
---
## Exercise Descriptions

### Exercise 1:
We implemented a recursive system to manage nested comment threads using a CommentNode structure. Each comment contains its id, user, content, likes, and a list of replies.

We created recursive functions to display the thread with indentation, count total comments, sum all likes, and find the deepest reply level. We also added search functions to find comments by user and detect keywords, as well as a deletion function that removes a comment and all its replies.

This exercise shows that recursion is well suited for hierarchical data like comment threads, as each reply can be processed in the same way as the main comment. 
### Exercise 2: Tree Traversals for Content Processing

The exercise focused on implementing classic binary tree traversals for a category hierarchy. In-order was used to display categories in sorted order, pre-order to export or serialize the tree, and post-order to aggregate metrics from children before processing parents. Additional analytics included finding the most popular category and the category with the most direct subcategories. A test script was included to run all traversals and print outputs, demonstrating practical applications like totals, leaf collection, and average depth.

### Exercise 3:  Generalized Trees (N-ary Trees) and Representations
This exercise focuses on the use of generalized trees (N-ary trees) to represent hierarchical category structures where each node can have multiple children. Recursive algorithms are implemented for tree traversals, height calculation, node and leaf counting, fan-out, and branching factor analysis. The exercise also explores the conversion between generalized trees and binary trees using the first child / next sibling representation, allowing the same hierarchy to be stored in different structural forms.

## Complexity Analysis Summary

Exercise, Time complexity, Space complexity
- Ex 1: O(n) for display, count, total likes, search, and deletion since each comment is visited once, O(n) also for finding deepest reply, space O(d) for recursion stack where d is the maximum nesting depth of the thread.
- Ex 2: O(n) for all traversals and analytics, space O(h) for recursion stack
- -Ex3 :The time complexity is O(n) for all traversals and metric calculations, as each node in the generalized tree is visited once. The conversion between generalized and binary trees also runs in O(n). The space complexity is O(d) for recursive methods, where d is the maximum tree depth, and O(n) for iterative breadth-first traversal using a queue.
- Ex 3: O(n), O(d)

