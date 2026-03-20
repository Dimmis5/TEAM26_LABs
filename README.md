# LAB_04 - Recursion

## Team 26
**Team Members:**
- Kamilla VAISOVA - Exercise 1 / 3
- Diméo ZHANG - Exercise x / 2
- Yannick ZHANG - Exercise x / 1
---
## Exercise Descriptions

### Exercise 1:

### Exercise 2: 
We implemented recursive functions to analyze post engagement using a divide-and-conquer approach. max_engagement finds the post with the highest engagement, sum_engagement and average_engagement compute total and average scores, count_above_threshold counts posts exceeding a threshold, and merge_sort_by_engagement sorts posts by engagement using recursive merge sort. Additionally, find_peak_hour identifies the hour with the most likes using a binary search-style recursion. We created example data with four posts and an hourly likes array, and all tests are at the end of the code to display maximum, total, and average engagement, count above threshold, sorted posts, and peak hour. The code is organized, modular, and demonstrates the divide-and-conquer strategy clearly.

### Exercise 3:  Recursion to Iteration
This exercise explores the use of recursion and its iterative equivalent for processing nested comment threads. A recursive approach is used to flatten a comment tree in depth-first order, demonstrating how naturally recursion handles hierarchical data structures. The same functionality is then implemented iteratively using an explicit stack, simulating the call stack to avoid recursion depth limitations.

Additionally, the exercise introduces tail recursion for counting comments and its conversion into a loop-based solution. This highlights the trade-offs between readability and control over memory usage, especially in systems where deep nesting may cause stack overflow.

## Complexity Analysis Summary

Exercise, Time complexity, Space complexity
- Ex 1: 
- Ex 2: Recursive Content Aggregation with Divide & Conquer, O(n) for max/sum/count, O(n log n) for merge sort, O(log n) for peak hour, space O(log n) for recursion stack plus O(n) extra for merge arrays.
- Ex 3: O(n), O(d)

