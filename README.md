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
This code simulates a simplified social media activity feed system using two data structures: a stack and a queue. The stack stores the user’s recent activities (like, comment, share, follow) following the LIFO principle, with functions to add, remove, view, and undo actions. The queue manages incoming notifications using the FIFO principle, allowing notifications to be added, processed, and displayed, with an option to add urgent notifications with priority. Finally, the FeedProcessor class combines these structures to process notifications, convert them into recent activities, archive processed items, and provide statistics about the system.

### Exercise 3:  

---

## Complexity Analysis Summary

Exercise, Time complexity, Space complexity
- Ex 1: Content Feed Navigation with Doubly Linked List, time O(n) for most but O(n²) for reorder_by_views, space O(n) because of prev and next
- Ex 2: Activity Feed Processing with Stacks and Queues, O(1) per push/pop/enqueue/dequeue, O(n) Stack and queue store up to n activities/notifications; undo stack and processed log also use linear space
- Ex 3: 

