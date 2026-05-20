def maximize_reach_exact(budget, costs, reaches):
    N = len(costs)
    dp = [[0] * (budget + 1) for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        user_cost = costs[i - 1]
        user_reach = reaches[i - 1]
        for w in range(budget + 1):
            if user_cost <= w:
                dp[i][w] = max(dp[i - 1][w], user_reach + dp[i - 1][w - user_cost])
            else:
                dp[i][w] = dp[i - 1][w]
                
    max_reach = dp[N][budget]
    
    selected_users_list = []
    w = budget
    for i in range(N, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_users_list.append(i - 1)
            w -= costs[i - 1]
            
    selected_users_list.reverse()
    return max_reach, selected_users_list


def is_within_budget(selection, costs, budget):
    total_cost = sum(costs[user_id] for user_id in selection)
    return total_cost <= budget


def maximize_reach_greedy(budget, costs, reaches):
    N = len(costs)
    user_data = []
    
    for i in range(N):
        ratio = reaches[i] / costs[i] if costs[i] > 0 else float('inf')
        user_data.append((i, costs[i], reaches[i], ratio))
        
    user_data.sort(key=lambda x: x[3], reverse=True)
    
    total_reach = 0
    budget_left = budget
    selected_users = []
    
    for user_id, cost, reach, ratio in user_data:
        if cost <= budget_left:
            selected_users.append(user_id)
            total_reach += reach
            budget_left -= cost
            
    selected_users.sort()
    return total_reach, selected_users


if __name__ == "__main__":
    print("VALIDATION TESTS - EXERCISE 2: VIRAL MESSAGE TIMING")
    print("\n[TEST 1]: Theoretical Counterexample")
    budget_1 = 10
    costs_1 = [6, 5, 5]
    reaches_1 = [7, 5, 5]
    reach_exact_1, users_exact_1 = maximize_reach_exact(budget_1, costs_1, reaches_1)
    reach_greedy_1, users_greedy_1 = maximize_reach_greedy(budget_1, costs_1, reaches_1) 
    valid_exact_1 = is_within_budget(users_exact_1, costs_1, budget_1)
    valid_greedy_1 = is_within_budget(users_greedy_1, costs_1, budget_1)
    print(f"Config: Budget = {budget_1} | Costs = {costs_1} | Reaches = {reaches_1}")
    print(f"-> Exact Solution (DP): Reach = {reach_exact_1} | Users = {users_exact_1} | Budget OK? {valid_exact_1}")
    print(f"-> Greedy Solution    : Reach = {reach_greedy_1} | Users = {users_greedy_1} | Budget OK? {valid_greedy_1}")
    print(f"Analysis: Exact beats Greedy by {reach_exact_1 - reach_greedy_1} reach points.")
    print("\n[TEST 2]: Random Dataset Instance (N = 20)")
    import random
    random.seed(42) 
    N_2 = 20
    budget_2 = 100
    costs_2 = [random.randint(5, 30) for _ in range(N_2)]
    reaches_2 = [random.randint(10, 100) for _ in range(N_2)]
    reach_exact_2, users_exact_2 = maximize_reach_exact(budget_2, costs_2, reaches_2)
    reach_greedy_2, users_greedy_2 = maximize_reach_greedy(budget_2, costs_2, reaches_2)
    valid_exact_2 = is_within_budget(users_exact_2, costs_2, budget_2)
    valid_greedy_2 = is_within_budget(users_greedy_2, costs_2, budget_2)
    print(f"Config: Budget = {budget_2} | N = {N_2} users")
    print(f"-> Exact Solution (DP): Reach = {reach_exact_2} | {len(users_exact_2)} users | Budget OK? {valid_exact_2}")
    print(f"-> Greedy Solution    : Reach = {reach_greedy_2} | {len(users_greedy_2)} users | Budget OK? {valid_greedy_2}")
    efficiency = (reach_greedy_2 / reach_exact_2) * 100
    print(f"Analysis: Greedy approximation achieves {efficiency:.2f}% of the optimal solution.")
