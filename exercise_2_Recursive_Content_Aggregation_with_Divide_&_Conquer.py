#Part A – Maximum Engagement

def max_engagement(posts, left, right):
    if left == right:
        return posts[left]['engagement_score']
    mid = (left + right) // 2
    max_left = max_engagement(posts, left, mid)
    max_right = max_engagement(posts, mid + 1, right)
    return max(max_left, max_right)

#Part B – Sum and Average Engagement

def sum_engagement(posts, left, right):
    if left == right:
        return posts[left]['engagement_score']
    mid = (left + right) // 2
    return sum_engagement(posts, left, mid) + sum_engagement(posts, mid + 1, right)

def average_engagement(posts, left, right):
    total = sum_engagement(posts, left, right)
    return total / (right - left + 1)

#Part C – Count Above Threshold

def count_above_threshold(posts, left, right, threshold):
    if left == right:
        return 1 if posts[left]['engagement_score'] > threshold else 0
    mid = (left + right) // 2
    return count_above_threshold(posts, left, mid, threshold) + \
           count_above_threshold(posts, mid + 1, right, threshold)

#Part D – Merge Sort by Engagement

def merge_sort_by_engagement(posts, left, right):
    if left == right:
        return [posts[left]]
    mid = (left + right) // 2
    left_sorted = merge_sort_by_engagement(posts, left, mid)
    right_sorted = merge_sort_by_engagement(posts, mid + 1, right)
    return merge(left_sorted, right_sorted)

def merge(left_array, right_array):
    result = []
    i = j = 0
    while i < len(left_array) and j < len(right_array):
        if left_array[i]['engagement_score'] > right_array[j]['engagement_score']:
            result.append(left_array[i])
            i += 1
        else:
            result.append(right_array[j])
            j += 1
    result.extend(left_array[i:])
    result.extend(right_array[j:])
    return result

#Part E – Find Peak Hour
def find_peak_hour(likes, left, right):
    mid = (left + right) // 2
    if mid == 0:
        return 0 if likes[0] >= likes[1] else 1
    if mid == len(likes) - 1:
        return len(likes) - 1 if likes[-1] >= likes[-2] else len(likes) - 2
    if likes[mid] >= likes[mid - 1] and likes[mid] >= likes[mid + 1]:
        return mid
    elif likes[mid - 1] > likes[mid]:
        return find_peak_hour(likes, left, mid - 1)
    else:
        return find_peak_hour(likes, mid + 1, right)
    
#Test


posts = [
    {"post_id": 1, "user_id": 101, "content_preview": "Post 1", "timestamp": "2026-03-18 08:00",
     "likes": 50, "comments": 40, "shares": 20, "engagement_score": 50*1 + 40*2 + 20*3},
    {"post_id": 2, "user_id": 102, "content_preview": "Post 2", "timestamp": "2026-03-18 09:00",
     "likes": 80, "comments": 60, "shares": 20, "engagement_score": 80*1 + 60*2 + 20*3},
    {"post_id": 3, "user_id": 103, "content_preview": "Post 3", "timestamp": "2026-03-18 10:00",
     "likes": 30, "comments": 25, "shares": 5, "engagement_score": 30*1 + 25*2 + 5*3},
    {"post_id": 4, "user_id": 104, "content_preview": "Post 4", "timestamp": "2026-03-18 11:00",
     "likes": 60, "comments": 50, "shares": 30, "engagement_score": 60*1 + 50*2 + 30*3},
]

hourly_likes = [5, 8, 12, 25, 30, 28, 15, 10, 8, 6, 5, 3, 2, 4, 6, 10, 12, 14, 16, 18, 15, 12, 10, 8]


print("Max Engagement:", max_engagement(posts, 0, len(posts)-1))
print("Total Engagement:", sum_engagement(posts, 0, len(posts)-1))
print("Average Engagement:", average_engagement(posts, 0, len(posts)-1))
print("Count Above 200:", count_above_threshold(posts, 0, len(posts)-1, 200))

sorted_posts = merge_sort_by_engagement(posts, 0, len(posts)-1)
print("Posts Sorted by Engagement:", [p['engagement_score'] for p in sorted_posts])

print("Peak Hour:", find_peak_hour(hourly_likes, 0, len(hourly_likes)-1))