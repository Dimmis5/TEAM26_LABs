class StoryNode:
    def __init__(self, story_id, user_id, content_preview, timestamp):
        self.story_id = story_id
        self.user_id = user_id
        self.content_preview = content_preview
        self.timestamp = timestamp
        self.views = 0
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.size = 0

    def add_story(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            self.current = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1

    def remove_story(self, story_id):
        node = self.head
        while node is not None:
            if node.story_id == story_id:
                if node.prev is not None:
                    node.prev.next = node.next
                else:
                    self.head = node.next
                if node.next is not None:
                    node.next.prev = node.prev
                else:
                    self.tail = node.prev
                if self.current == node:
                    self.current = node.next
                self.size -= 1
                return node
            node = node.next

    def move_forward(self):
        if self.current and self.current.next is not None:
            self.current = self.current.next
        return self.current

    def move_backward(self):
        if self.current and self.current.prev is not None:
            self.current = self.current.prev
        return self.current

    def jump_to(self, story_id):
        node = self.head
        while node is not None:
            if node.story_id == story_id:
                self.current = node
                return node
            node = node.next
        return None

    def insert_after(self, current_id, new_story):
        node = self.head
        while node is not None:
            if node.story_id == current_id:
                new_story.next = node.next
                new_story.prev = node
                if node.next is not None:
                    node.next.prev = new_story
                else:
                    self.tail = new_story
                node.next = new_story
                self.size += 1
                return
            node = node.next

    def display_around_current(self, k):
        temp = self.current
        count = 0
        while temp.prev is not None and count < k:
            temp = temp.prev
            count += 1
        printed = 0
        while temp is not None and printed < (2 * k + 1):
            print(temp.story_id)
            temp = temp.next
            printed += 1

    def track_view(self):
        if self.current is not None:
            self.current.views += 1
            return self.current.views

    def most_viewed(self):
        node = self.head
        max_view = self.head
        while node is not None:
            if node.views > max_view.views:
                max_view = node
            node = node.next
        return max_view
        
    def reorder_by_views(self):
        if self.head is None:
             return
        swapped = True
        while swapped:
               swapped = False
               node = self.head
               while node.next is not None:
                    if node.views < node.next.views:
                         node.story_id, node.next.story_id = node.next.story_id, node.story_id
                         node.user_id, node.next.user_id = node.next.user_id, node.user_id
                         node.content_preview, node.next.content_preview = node.next.content_preview, node.content_preview
                         node.timestamp, node.next.timestamp = node.next.timestamp, node.timestamp
                         node.views, node.next.views = node.next.views, node.views
                         swapped = True
                    node = node.next
                    

# test cases
feed = DoublyLinkedList()

s1 = StoryNode(1, 101, "Morning coffee", "08:00")
s2 = StoryNode(2, 102, "Workout complete", "09:00")
s3 = StoryNode(3, 103, "Sunset photo", "19:00")

feed.add_story(s1)
feed.add_story(s2)
feed.add_story(s3)

feed.jump_to(2)
feed.track_view()
feed.track_view()

feed.jump_to(3)
feed.track_view()

print("Most viewed:", feed.most_viewed().story_id)

feed.reorder_by_views()

node = feed.head
while node:
    print(node.story_id, node.views)
    node = node.next