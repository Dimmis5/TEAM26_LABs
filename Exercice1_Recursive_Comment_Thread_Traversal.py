class CommentNode:
    def __init__(self, comment_id, user_id, content, timestamp, likes):
        self.comment_id = comment_id
        self.user_id = user_id
        self.content = content
        self.timestamp = timestamp
        self.likes = likes
        self.replies = []


def display_thread(comment, level):
    print(" " * (2 * level) + comment.content)
    for reply in comment.replies:
        display_thread(reply, level + 1)


def count_total_comments(comment):
    count = 0
    for reply in comment.replies:
        count += count_total_comments(reply)
    return count + 1


def total_likes(comment):
    like_count = comment.likes
    for reply in comment.replies:
        like_count += total_likes(reply)
    return like_count


def find_deepest_reply(comment):
    deepestmax = 0
    for reply in comment.replies:
        depth = find_deepest_reply(reply)
        if depth > deepestmax:
            deepestmax = depth
    return deepestmax + 1


def search_by_user(user_id, comment):
    result = []
    if comment.user_id == user_id:
        result.append(comment)
    for reply in comment.replies:
        result.extend(search_by_user(user_id, reply))
    return result


def contains_keyword(keyword, comment):
    if keyword in comment.content:
        return True
    for reply in comment.replies:
        if contains_keyword(keyword, reply):
            return True
    return False


def delete_comment(comment_id, thread):
    if thread.comment_id == comment_id:
        return None

    new_replies = []
    for reply in thread.replies:
        updated_reply = delete_comment(comment_id, reply)
        if updated_reply is not None:
            new_replies.append(updated_reply)

    thread.replies = new_replies
    return thread


root = CommentNode(1, 100, "Main post", "2025-01-01", 10)
r1 = CommentNode(2, 101, "First reply", "2025-01-02", 3)
r2 = CommentNode(3, 102, "Second reply keyword", "2025-01-03", 5)
r3 = CommentNode(4, 101, "Nested reply", "2025-01-04", 2)
r4 = CommentNode(5, 103, "Deep keyword reply", "2025-01-05", 1)

root.replies = [r1, r2]
r1.replies = [r3]
r3.replies = [r4]

print("DISPLAY THREAD")
display_thread(root, 0)

print("\nCOUNT TOTAL COMMENTS")
print(count_total_comments(root))
print(count_total_comments(CommentNode(10, 200, "Only one", "2025-01-01", 0)))

print("\nTOTAL LIKES")
print(total_likes(root))
print(total_likes(CommentNode(11, 201, "No replies", "2025-01-01", 7)))

print("\nFIND DEEPEST REPLY")
print(find_deepest_reply(root))
print(find_deepest_reply(CommentNode(12, 202, "Single node", "2025-01-01", 0)))

print("\nSEARCH BY USER")
matches = search_by_user(101, root)
print([node.comment_id for node in matches])

matches_none = search_by_user(999, root)
print([node.comment_id for node in matches_none])

print("\nCONTAINS KEYWORD")
print(contains_keyword("keyword", root))
print(contains_keyword("missing", root))
print(contains_keyword("", root))

print("\nDELETE COMMENT")
new_root = delete_comment(4, root)
display_thread(new_root, 0)

print("\nDELETE LEAF COMMENT")
root2 = CommentNode(1, 100, "Main post", "2025-01-01", 10)
a = CommentNode(2, 101, "Reply A", "2025-01-02", 1)
b = CommentNode(3, 102, "Reply B", "2025-01-03", 1)
root2.replies = [a, b]
new_root2 = delete_comment(3, root2)
display_thread(new_root2, 0)

print("\nDELETE ROOT COMMENT")
root3 = CommentNode(1, 100, "Root", "2025-01-01", 0)
c = CommentNode(2, 101, "Child", "2025-01-02", 0)
root3.replies = [c]
new_root3 = delete_comment(1, root3)
print(new_root3)

print("\nDELETE NON-EXISTENT COMMENT")
root4 = CommentNode(1, 100, "Root", "2025-01-01", 0)
d = CommentNode(2, 101, "Child", "2025-01-02", 0)
root4.replies = [d]
new_root4 = delete_comment(999, root4)
display_thread(new_root4, 0)