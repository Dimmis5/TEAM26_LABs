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

