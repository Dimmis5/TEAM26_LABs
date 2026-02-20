class FollowerMatrix:
    def __init__(self, size):
        self.matrix = [[False for _ in range(size)] for _ in range(size)]
        self.size = size
        self.user_count = size

    def follow(self, follower, followee):
        self.matrix[follower - 1][followee - 1] = True

    def unfollow(self, follower, followee):
        self.matrix[follower - 1][followee - 1] = False

    def is_following(self, follower, followee):
        return self.matrix[follower - 1][followee - 1]

    def get_following(self, user):
        following_list = []
        user_idex = user - 1
        for j in range(self.size):
            if self.matrix[user_idex][j]:
                following_list.append(j + 1)
        return following_list

    def get_followers(self, user):
        followers_list = []
        user_idex = user - 1
        for i in range(self.size):
            if self.matrix[i][user_idex]:
                followers_list.append(i + 1)
        return followers_list

    def find_mutual_follows(self):
        mutuals = []
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if self.matrix[i][j] and self.matrix[j][i]:
                    mutuals.append((i + 1, j + 1))
        return mutuals

    def calculate_influence_score(self, user):
        followers_count = len(self.get_followers(user))
        following_count = len(self.get_following(user))
        score = (followers_count + following_count) / self.user_count
        return round(score, 2)

def print_matrix(fm):
    for row in fm.matrix:
        print(" ".join(['T' if x else 'F' for x in row]))


#Exemple of the statement

social_graph = FollowerMatrix(3)

social_graph.follow(1, 2) 
social_graph.follow(2, 1) 
social_graph.follow(2, 3) 

print("Matrice de suivi (T=True, F=False) :")
for row in social_graph.matrix:
    print(['T' if x else 'F' for x in row])

print(f"\nFollows mutuels : {social_graph.find_mutual_follows()}")

for u in range(1, 4):
    score = social_graph.calculate_influence_score(u)
    print(f"Influence Score User{u} : {score}/1.0")

# TEST SET

print("TEST 1: SINGLE USER")
test1 = FollowerMatrix(1)
print_matrix(test1)
print(f"Mutuals: {test1.find_mutual_follows()}")
print(f"Influence Score: {test1.calculate_influence_score(1)}")

print("\nTEST 2: SELF-FOLLOWING ")
test2 = FollowerMatrix(3)
test2.follow(1, 1)
print_matrix(test2)
print(f"Mutuals : {test2.find_mutual_follows()}")
print(f"Score User 1 : {test2.calculate_influence_score(1)}")

print("\nTEST 3: NO MUTUALS FOLLOWING ")
test3 = FollowerMatrix(3)
test3.follow(1, 2)
test3.follow(2, 3)
test3.follow(3, 1)
print_matrix(test3)
print(f"Mutuals: {test3.find_mutual_follows()}")

print("\nTEST 4: BOUNDARY USERS")
N = 5
test4 = FollowerMatrix(N)
test4.follow(1, N)
test4.follow(N, 1) 
print_matrix(test4)
print(f"Mutuals: {test4.find_mutual_follows()}")

print("\nTEST 5: FOLLOW THEN UNFOLLOW ")
test5 = FollowerMatrix(2)
test5.follow(1, 2)
print("Before Unfollow:")
print_matrix(test5)
test5.unfollow(1, 2)
print("After Unfollow:")
print_matrix(test5)
print(f"Is User 1 still following 2? {test5.is_following(1, 2)}")

print("\nTEST 6: EVERYONE FOLLOWS EVERYONE")
test6 = FollowerMatrix(3)
for i in range(1, 4):
    for j in range(1, 4):
        test6.follow(i, j)
print_matrix(test6)
print(f"Mutuals: {test6.find_mutual_follows()}")
print(f"Influence Score User 1: {test6.calculate_influence_score(1)}")