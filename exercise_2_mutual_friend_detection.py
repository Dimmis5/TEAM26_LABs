def mutual(set1,set2):
	return set1.intersection(set2)
def unique(set1,set2):
	return set1.difference(set2)
def total(set1,set2):
	return set1.union(set2)
def jaccard(set1,set2):
	mutual_friends = mutual(set1,set2)
	union_friends = total(set1,set2)
	if len(union_friends) == 0:
		return 0
	similarity_coeff = len(mutual_friends)/len(union_friends)
	return similarity_coeff
def suggest(user_id, all_users_friends):
	user_friends = all_users_friends[user_id]
	suggestions = []
	for friend in user_friends:
		friends_of_friend = all_users_friends[friend]
		for person in friends_of_friend:
			if person != user_id and person not in user_friends:
				suggestions.add(person)
	return suggestions

User_A_friends = {101, 102, 103, 104, 105}
User_B_friends = {103, 104, 106, 107, 108}
print("Mutual friends:", mutual(User_A_friends, User_B_friends))
print("Unique friends of User A:", unique(User_A_friends, User_B_friends))
print("Unique friends of User B:", unique(User_B_friends, User_A_friends))
print("Total friends:", total(User_A_friends, User_B_friends))
print("Jaccard similarity coefficient:", jaccard(User_A_friends, User_B_friends))




