# LAB_01 - Revision

## Team 26
**Team Members:**
- Kamilla VAISOVA - Exercises 2, 4
- Diméo ZHANG - Exercises 2
- Yannick ZHANG - Exercises 1, 6

---
## Exercise Descriptions

### Exercise 1: Integer Mirror (Digit Reversal)
To reverse a number without converting it into a string, we have to isolate each digit by using modulo, then add it back mathematically. In this exercise, we observed that the time complexity depends mainly on the length (number of digits) of the integer.

### Exercise 2: Activity Feed Processing with Stacks and Queues
This code simulates a simplified social media activity feed system using two data structures: a stack and a queue. The stack stores the user’s recent activities (like, comment, share, follow) following the LIFO principle, with functions to add, remove, view, and undo actions. The queue manages incoming notifications using the FIFO principle, allowing notifications to be added, processed, and displayed, with an option to add urgent notifications with priority. Finally, the FeedProcessor class combines these structures to process notifications, convert them into recent activities, archive processed items, and provide statistics about the system.

### Exercise 3: Merge Overlapping Intervals
To merge overlapping intervals, we first sort all intervals by their start value. This allows us to process them in order from left to right. We then keep track of the current merged interval as we scan through the sorted list. For each new interval, we check if it overlaps with our current interval (by comparing if the new start is less than or equal to the current end). If they overlap, we extend the current interval's end to cover both. If they don't overlap, we save the current interval and start a new one. This approach ensures we only need one pass through the data after sorting.

---

## Complexity Analysis Summary

Exercise, Time complexity, Space complexity
- Ex 1: Integer Mirror, O(log n), O(1), Loop runs once per digit; d digits = log₁₀(n)
- Ex 2: Activity Feed Processing with Stacks and Queues, O(1) per push/pop/enqueue/dequeue, O(n) Stack and queue store up to n activities/notifications; undo stack and processed log also use linear space
- Ex 3: Merge Intervals, O(n log n), O(n), Dominated by sorting; linear merge afterward

