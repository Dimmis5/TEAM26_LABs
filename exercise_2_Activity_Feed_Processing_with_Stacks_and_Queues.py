# Part A - Activity Stack

class ActivityNode:
    def __init__(self, activity):
        self.activity = activity
        self.next = None


class ActivityStack:
    def __init__(self):
        self.top = None
        self.count = 0
        self.undo_stack = []

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.count

    def push(self, activity):
        new_node = ActivityNode(activity)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            return None

        removed = self.top
        self.top = self.top.next
        self.count -= 1
        return removed.activity

    def peek(self):
        if self.is_empty():
            return None
        return self.top.activity

    def display_recent(self, n):
        current = self.top
        i = 0

        while current and i < n:
            print(current.activity)
            current = current.next
            i += 1

    def undo_last(self):
        activity = self.pop()
        if activity:
            self.undo_stack.append(activity)
            print("Undo:", activity)
        else:
            print("Nothing to undo")

    def redo(self):
        if not self.undo_stack:
            print("Nothing to redo")
            return

        activity = self.undo_stack.pop()
        self.push(activity)
        print("Redo:", activity)

# Part B - Notifications Queue

class NotificationNode:
    def __init__(self, notification):
        self.notification = notification
        self.next = None


class NotificationQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def is_empty(self):
        return self.front is None

    def size(self):
        return self.count

    def enqueue(self, notification):
        new_node = NotificationNode(notification)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.count += 1

    def dequeue(self):
        if self.is_empty():
            return None

        temp = self.front
        notification = temp.notification
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self.count -= 1
        return notification

    def front_item(self):
        if self.is_empty():
            return None
        return self.front.notification

    def display_pending(self):
        current = self.front
        while current:
            print(current.notification)
            current = current.next

    def priority_enqueue(self, notification):
        new_node = NotificationNode(notification)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            new_node.next = self.front
            self.front = new_node

        self.count += 1


#Part C - FeedProcessor

class FeedProcessor:
    def __init__(self):
        self.recent_activities = ActivityStack()
        self.notification_queue = NotificationQueue()
        self.processed_log = NotificationQueue()

    def process_incoming(self):
        notification = self.notification_queue.dequeue()

        if notification:
            self.recent_activities.push(notification)
        else:
            print("No notifications to process")

    def batch_process(self, k):
        for _ in range(k):
            if self.notification_queue.is_empty():
                break

            notification = self.notification_queue.dequeue()
            self.recent_activities.push(notification)

    def clear_history(self):
        while not self.recent_activities.is_empty():
            activity = self.recent_activities.pop()
            self.processed_log.enqueue(activity)

    def get_stats(self):
        return {
            "recent_activities": self.recent_activities.size(),
            "pending_notifications": self.notification_queue.size(),
            "processed_items": self.processed_log.size()
        }
    


#Test

feed = FeedProcessor()

feed.notification_queue.enqueue("New follower")
feed.notification_queue.enqueue("New like")
feed.notification_queue.enqueue("New comment")

feed.recent_activities.push("Shared photo")
feed.recent_activities.push("Commented on post")
feed.recent_activities.push("Liked video")

print("Recent activities:")
feed.recent_activities.display_recent(5)

print("\nProcessing incoming notification...")
feed.process_incoming()

print("\nRecent activities after processing:")
feed.recent_activities.display_recent(5)

print("\nPending notifications:")
feed.notification_queue.display_pending()

print("\nStats:")
print(feed.get_stats())