# LAB_01 - Revision

## Team 26
**Team Members:**
- Kamilla VAISOVA - Exercises 
- Diméo ZHANG - Exercises 1
- Yannick ZHANG - Exercises 

---
## Exercise Descriptions

### Exercise 1: Friend Request Timeline
The proposed solution follows a modular design by breaking down the messaging analysis into four distinct functions—counting uppercase letters, total alphabetic characters, specific punctuation marks, and detecting character repetitions—which allows each feature to be tested and maintained independently for better code clarity. This modular structure is orchestrated by a main function that calculates the "caps ratio" and applies specific logical thresholds to classify messages as CALM, URGENT, or AGGRESSIVE, while also flagging potential spam if any character is repeated more than three times consecutively. 

### Exercise 2: Balanced Symbol Checker
To validate whether parentheses, brackets, and braces are properly balanced and nested, we use a stack data structure. We push opening symbols onto a stack. When encountering a closing symbol, 
we check if it matches the top of the stack. If the stack is empty, it means there is a pairless closing symbol, or if the closing does not match the opening, it returns False. The string is balanced if stack is empty at the end, meaning that with each closing symbol, an opening symbol was popped out of the stack.

### Exercise 3: Merge Overlapping Intervals
To merge overlapping intervals, we first sort all intervals by their start value. This allows us to process them in order from left to right. We then keep track of the current merged interval as we scan through the sorted list. For each new interval, we check if it overlaps with our current interval (by comparing if the new start is less than or equal to the current end). If they overlap, we extend the current interval's end to cover both. If they don't overlap, we save the current interval and start a new one. This approach ensures we only need one pass through the data after sorting.

### Exercise 4: Mutual Followers Matrix

---

## Complexity Analysis Summary

Exercise, Time complexity, Space complexity
- Ex 1: Friend Request Timeline, O (n), O(1), Loops traverse the n -character string to count patterns.
- Ex 2: Balanced Symbols, O(n), O(n), Single pass; stack stores up to n/2 elements
- Ex 3: Merge Intervals, O(n log n), O(n), Dominated by sorting; linear merge afterward
- Ex 4: Mutual Followers Matrix,