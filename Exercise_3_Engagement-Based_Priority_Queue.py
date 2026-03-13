class Post:
    def __init__(self, post_id, likes, comments, shares, timestamp):
        self.post_id = post_id
        self.likes = likes
        self.comments = comments
        self.shares = shares
        self.timestamp = timestamp
        self.engagement_score = 0
    
    def __str__(self):
        return f"[Post {self.post_id} | Score: {self.engagement_score} | Time: {self.timestamp}]"

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        curr = self.head
        while curr is not None:
            curr = curr.next
            count += 1
        return count

    def enqueue(self, p, recalculate=True):
        if recalculate:
            compute = (p.likes * 1) + (p.comments * 2) + (p.shares * 3)
            p.engagement_score = compute
            
        node = Node(p)
        curr = self.head

        if curr is None or curr.value.engagement_score < p.engagement_score:
            node.next = curr
            self.head = node
            return
        
        ahead = curr.next
        while ahead is not None and ahead.value.engagement_score >= p.engagement_score:
            curr = curr.next
            ahead = curr.next
            
        curr.next = node
        node.next = ahead

    def dequeue_max(self):
        if self.head is None:
            return None
        
        to_dequeue = self.head
        saved_post = to_dequeue.value
        self.head = self.head.next
        return saved_post

    def peek_max(self):
        if self.head is None:
            return None
        return self.head.value

    def update_score(self, post_id, new_likes, new_comments, new_shares):
        curr = None
        ahead = self.head
        
        while ahead is not None and ahead.value.post_id != post_id:
            curr = ahead
            ahead = ahead.next
            
        if ahead is None:
            return
            
        ahead.value.likes = new_likes
        ahead.value.comments = new_comments
        ahead.value.shares = new_shares
        
        if curr is None:
            self.head = ahead.next
        else:
            curr.next = ahead.next
            
        saved_post = ahead.value
        self.enqueue(saved_post)

    def refresh_all(self):
        new_queue = PriorityQueue()
        curr = self.head
        while curr is not None:
            new_queue.enqueue(curr.value, recalculate=False) 
            curr = curr.next
        self.head = new_queue.head

    def get_top_k(self, k):
        top_posts = []
        curr = self.head
        limit = min(k, self.size())
        
        for _ in range(limit):
            top_posts.append(curr.value)
            curr = curr.next
            
        return top_posts

    def decay_older_than(self, time_limit):
        curr = self.head
        
        while curr is not None:
            if curr.value.timestamp < time_limit:
                old_score = curr.value.engagement_score
                curr.value.engagement_score = old_score - 5
            curr = curr.next
            
        self.refresh_all()

    def display_queue(self):
        curr = self.head
        if curr is None:
            print("The queue is empty.")
            return
        path = ""
        while curr is not None:
            path += f"{curr.value} -> "
            curr = curr.next
        print(path + "null")
        
my_queue = PriorityQueue()

post1 = Post("A01", likes=20, comments=0, shares=0, timestamp=10)
post2 = Post("B02", likes=18, comments=0, shares=0, timestamp=50)
post3 = Post("C03", likes=17, comments=0, shares=0, timestamp=60)
post4 = Post("D04", likes=5,  comments=0, shares=0, timestamp=70)

my_queue.enqueue(post1)
my_queue.enqueue(post2)
my_queue.enqueue(post3)
my_queue.enqueue(post4)

print("1. Initial state:")
my_queue.display_queue()

print("\n2. Top 2 posts:")
top_2 = my_queue.get_top_k(2)
for i, post in enumerate(top_2):
    print(f"  #{i+1} -> {post}")

my_queue.decay_older_than(30)

print("\n3. State after Time Decay (timestamp < 30 lose 5 points):")
my_queue.display_queue()

print("\n4. New Top 2 posts:")
new_top_2 = my_queue.get_top_k(2)
for i, post in enumerate(new_top_2):
    print(f"  #{i+1} -> {post}")