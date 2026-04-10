# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 20:00:19 2026

@author: turet
"""

from collections import deque


class SocialGraph:
    def __init__(self):
        self.graph = {}

    def add_user(self, user):
        if user not in self.graph:
            self.graph[user] = []

    def add_friendship(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        if v not in self.graph[u]:
            self.graph[u].append(v)
        if u not in self.graph[v]:
            self.graph[v].append(u)

    def get_num_users(self):
        return len(self.graph)

    def get_friends(self, user):
        if user not in self.graph:
            return []
        return self.graph[user]

    def bfs(self, start_user):
        if start_user not in self.graph:
            return []

        visited = {}
        queue = deque([start_user])
        order = []

        while len(queue) != 0:
            value = queue.popleft()

            if value not in visited:
                visited[value] = True
                order.append(value)

                for v in self.graph[value]:
                    if v not in visited:
                        queue.append(v)

        return order

    def bfs_with_distances(self, start_user):
        if start_user not in self.graph:
            return {}

        visited = {}
        queue = deque([start_user])
        distance = {}

        visited[start_user] = True
        distance[start_user] = 0

        while len(queue) != 0:
            value = queue.popleft()

            for v in self.graph[value]:
                if v not in visited:
                    visited[v] = True
                    distance[v] = distance[value] + 1
                    queue.append(v)

        return distance

    def shortest_path(self, start_user, target_user):
        if start_user not in self.graph or target_user not in self.graph:
            return []

        if start_user == target_user:
            return [start_user]

        visited = {}
        queue = deque()
        predecessors = {}

        visited[start_user] = True
        queue.append(start_user)
        predecessors[start_user] = None

        while len(queue) != 0:
            current = queue.popleft()

            if current == target_user:
                path = []
                step = target_user

                while step is not None:
                    path.insert(0, step)
                    step = predecessors[step]

                return path

            for v in self.graph[current]:
                if v not in visited:
                    visited[v] = True
                    predecessors[v] = current
                    queue.append(v)

        return []

    def degrees_of_separation(self, start_user, target_user):
        if start_user not in self.graph or target_user not in self.graph:
            return -1

        distance = self.bfs_with_distances(start_user)

        if target_user in distance:
            return distance[target_user]
        else:
            return -1

    def friends_within_k_hops(self, start_user, k):
        if start_user not in self.graph:
            return set()

        if k < 0:
            return set()

        distance = self.bfs_with_distances(start_user)
        tab = set()

        for key, value in distance.items():
            if value <= k:
                tab.add(key)

        return tab

    def compute_average_degrees_of_separation(self):
        user_list = list(self.graph.keys())
        total_sum = 0
        divide = 0

        for u in user_list:
            distance = self.bfs_with_distances(u)

            for v, dist in distance.items():
                if v != u:
                    total_sum += dist
                    divide += 1

        if divide != 0:
            return total_sum / divide

        return 0

    def get_distance_distribution(self, start_user):
        if start_user not in self.graph:
            return {}

        distance = self.bfs_with_distances(start_user)
        distribution = {}

        for user, value in distance.items():
            if value > 0:
                if value not in distribution:
                    distribution[value] = 1
                else:
                    distribution[value] += 1

        return distribution

    def recommend_friends(self, start_user, max_recommendations=5):
        if start_user not in self.graph:
            return []

        if max_recommendations <= 0:
            return []

        distance = self.bfs_with_distances(start_user)
        recommendation = []

        for user, value in distance.items():
            if value == 2:
                recommendation.append(user)
                if len(recommendation) == max_recommendations:
                    break

        return recommendation
g = SocialGraph()

g.add_friendship("A", "B")
g.add_friendship("A", "C")
g.add_friendship("B", "D")
g.add_friendship("C", "E")
g.add_friendship("D", "F")
g.add_friendship("E", "F")
g.add_user("Z")  

print("BFS from A:", g.bfs("A"))
print("Distances from A:", g.bfs_with_distances("A"))
print("Shortest path A -> F:", g.shortest_path("A", "F"))
print("Degrees of separation A -> F:", g.degrees_of_separation("A", "F"))
print("Users within 2 hops from A:", g.friends_within_k_hops("A", 2))
print("Average degrees of separation:", g.compute_average_degrees_of_separation())
print("Distance distribution from A:", g.get_distance_distribution("A"))
print("Recommendations for A:", g.recommend_friends("A", 5))

print("Shortest path A -> Z:", g.shortest_path("A", "Z"))
print("Degrees of separation A -> Z:", g.degrees_of_separation("A", "Z"))
print("BFS from unknown user:", g.bfs("X"))