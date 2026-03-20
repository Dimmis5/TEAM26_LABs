def flatten_recursive(comment):
    if comment is None:
        return []
    result = [comment]
    for reply in comment.replies:
        result.extend(flatten_recursive(reply))
    return result

def flatten_iterative(comment):
    result = []
    stack = [(comment, 'STATE_START')]
    while stack:
        comment, state = stack.pop()
        if comment is None:
            continue
        if state == 'STATE_START':
            # Add the current comment to result
            result.append(comment)
            # Coming back after recursion
            stack.append((comment, 'STATE_REPLIES_DONE'))
            # Push children onto the stack
            for reply in reversed(comment.replies):
                stack.append((reply, 'STATE_START'))
        elif state == 'STATE_REPLIES_DONE':
            continue

    return result

def count_comments_tail(comment, accumulator):
    if comment is None:
        return accumulator
    # Count the current node
    accumulator += 1
    # Process all replies
    for reply in comment.replies:
        accumulator = count_comments_tail(reply, accumulator)
    return accumulator


def count_comments_loop(comment):
    count = 0
    stack = []
    stack.append(comment)
    while stack:
        current_comment = stack.pop()
        if current_comment is None:
            continue
        count += 1
        for reply in current_comment.replies:
            stack.append(reply)
    return count


class Comment:
    def __init__(self, id):
        self.id = id
        self.replies = []

# Build tree
c1 = Comment(1)
c2 = Comment(2)
c3 = Comment(3)
c4 = Comment(4)
c5 = Comment(5)

c1.replies = [c2, c5]
c2.replies = [c3]
c3.replies = [c4]

# Structure:
# 1
# ├─ 2
# │   └─ 3
# │        └─ 4
# └─ 5

# Test flatten
print([c.id for c in flatten_recursive(c1)])
print([c.id for c in flatten_iterative(c1)])

# Test count
print(count_comments_tail(c1, 0))
print(count_comments_loop(c1))