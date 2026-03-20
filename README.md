# LAB_01 - Revision

## Team 26
**Team Members:**
- Kamilla VAISOVA - Exercise 1
- Diméo ZHANG - Exercise 2
- Yannick ZHANG - Exercise 3
---
## Exercise Descriptions

### Exercise 1: Content Feed Navigation with Doubly Linked List
This exercise implements a Content Feed Navigation system using a Doubly Linked List in Python. Each story in the feed is represented by a StoryNode containing information such as the story ID, author ID, content preview, timestamp, and view count. The feed itself is managed by a DoublyLinkedList that maintains pointers to the head, tail, and the currently viewed story. The implementation supports typical feed navigation operations such as adding and removing stories, moving forward and backward through the feed, jumping to a specific story, inserting a story after another, and displaying stories around the current position. It also includes engagement tracking features like incrementing story views, finding the most viewed story, and reordering the feed based on view counts.

### Exercise 2: Activity Feed Processing with Stacks and Queues
We implemented recursive functions to analyze post engagement using a divide-and-conquer approach. max_engagement finds the post with the highest engagement, sum_engagement and average_engagement compute total and average scores, count_above_threshold counts posts exceeding a threshold, and merge_sort_by_engagement sorts posts by engagement using recursive merge sort. Additionally, find_peak_hour identifies the hour with the most likes using a binary search-style recursion. We created example data with four posts and an hourly likes array, and all tests are at the end of the code to display maximum, total, and average engagement, count above threshold, sorted posts, and peak hour. The code is organized, modular, and demonstrates the divide-and-conquer strategy clearly.

### Exercise 3:  

This project implements the core engine for a social media 'Trending' feed, utilizing a custom Priority Queue built on a sorted linked list. Rather than ordering posts chronologically, the system dynamically ranks content based on a composite engagement score (driven by likes, comments, and shares). It handles standard queue operations—such as safely inserting posts into their correct ranked position and extracting the most viral content—but also includes advanced feed mechanics. The program can update a specific post's score on the fly by cleanly detaching and repositioning its node, simulate content aging through a time-decay penalty on older posts, and efficiently fetch the top K trending items. Overall, this code demonstrates how to maintain a complex, constantly shifting ranking system.

## Complexity Analysis Summary

Exercise, Time complexity, Space complexity
- Ex 1: Content Feed Navigation with Doubly Linked List, time O(n) for most but O(n²) for reorder_by_views, space O(n) because of prev and next
- Ex 2: Recursive Content Aggregation with Divide & Conquer, O(n) for max/sum/count, O(n log n) for merge sort, O(log n) for peak hour, space O(log n) for recursion stack plus O(n) extra for merge arrays.
- Ex 3: Trending Feed Processing with a Priority Queue (Sorted Linked List), O(N) per enqueue/update_score, O(1) per dequeue_max/peek, O(n) Sorted linked list stores up to n posts; temporary queue during refresh also uses linear space


