class SocialGraph:
    def __init__(self, num_users):
        self.num_users = num_users 
        self.num_edges = 0 
        
        self.adj_matrix = [[0 for _ in range(num_users)] for _ in range(num_users)]

        self.adj_list = {i: [] for i in range(num_users)}
    def add_friendship(self, u, v):
        if 0 <= u < self.num_users and 0 <= v < self.num_users and u != v:
            if self.adj_matrix[u][v] == 0:
                self.adj_matrix[u][v] = 1
                self.adj_matrix[v][u] = 1
                
                self.adj_list[u].append(v)
                self.adj_list[v].append(u)
                
                self.num_edges += 1

    def remove_friendship(self, u, v):
        if 0 <= u < self.num_users and 0 <= v < self.num_users:
            if self.adj_matrix[u][v] == 1:
                self.adj_matrix[u][v] = 0
                self.adj_matrix[v][u] = 0
                
                self.adj_list[u].remove(v)
                self.adj_list[v].remove(u)
                
                self.num_edges -= 1

    def are_friends(self, u, v):
        return self.adj_matrix[u][v] == 1

    def get_friends(self, u):
        return self.adj_list[u]

    def get_degree(self, u):
        return len(self.adj_list[u])

    def get_num_users(self):
        return self.num_users

    def get_num_edges(self):
        return self.num_edges


    def is_complete_graph(self):
        expected_edges = (self.num_users * (self.num_users - 1)) // 2
        return self.num_edges == expected_edges

    def graph_density(self):
        if self.num_users < 2:
            return 0.0
        return (2 * self.num_edges) / (self.num_users * (self.num_users - 1))

    def degree_distribution(self):
        distribution = {}
        for u in range(self.num_users):
            degree = self.get_degree(u)
            distribution[degree] = distribution.get(degree, 0) + 1
        return distribution

    def matrix_to_list(self):

        new_list = {i: [] for i in range(self.num_users)}
        for u in range(self.num_users):
            for v in range(u + 1, self.num_users):
                if self.adj_matrix[u][v] == 1:
                    new_list[u].append(v)
                    new_list[v].append(u)
        self.adj_list = new_list

    def list_to_matrix(self):
        new_matrix = [[0 for _ in range(self.num_users)] for _ in range(self.num_users)]
        for u, friends in self.adj_list.items():
            for v in friends:
                new_matrix[u][v] = 1
        self.adj_matrix = new_matrix

def test_social_graph():
    network = SocialGraph(5)
    network.add_friendship(0, 1)
    network.add_friendship(0, 2)
    network.add_friendship(1, 2)
    network.add_friendship(3, 4)
    
    print(f"Total users: {network.get_num_users()}") 
    print(f"Total edges: {network.get_num_edges()}") 
    
    print(f"Are 0 and 1 friends? {network.are_friends(0, 1)}") 
    print(f"Are 0 and 3 friends? {network.are_friends(0, 3)}") 
    
     
    print(f"Degree of user 0: {network.get_degree(0)}") 
    
    print("\n Testing Graph Properties")
    
        
    print(f"Graph density: {network.graph_density()}") 
    
    print(f"Is complete? {network.is_complete_graph()}") 
    print(f"Degree distribution: {network.degree_distribution()}") 

    print("\n Testing Conversions")
    
    network.matrix_to_list()
    print("Matrix to List conversion successful.")
    
    network.list_to_matrix()
    print("List to Matrix conversion successful.")

    network.remove_friendship(0, 1)
    print(f"After removal, are 0 and 1 friends? {network.are_friends(0, 1)}") 
    print(f"New total edges: {network.get_num_edges()}") 

if __name__ == "__main__":
    test_social_graph()