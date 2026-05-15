def maximize_reach(budget, costs, influences):
    n = len(costs)

    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for b in range(budget + 1):

            if costs[i - 1] > b:
                dp[i][b] = dp[i - 1][b]

            else:
                skip = dp[i - 1][b]
                take = influences[i - 1] + dp[i - 1][b - costs[i - 1]]

                dp[i][b] = max(skip, take)

    selected = []

    b = budget

    for i in range(n, 0, -1):

        if dp[i][b] != dp[i - 1][b]:
            selected.append(i - 1)
            b -= costs[i - 1]

    selected.reverse()

    return dp[n][budget], selected


def is_within_budget(selection, costs, budget):
    total = 0

    for user in selection:
        total += costs[user]

    return total <= budget


def fast_alternative_strategy(budget, costs, influences):
    n = len(costs)

    users = []

    for i in range(n):
        ratio = influences[i] / costs[i]
        users.append((ratio, i))

    users.sort(reverse=True)

    total_cost = 0
    total_influence = 0

    selected = []

    for ratio, i in users:

        if total_cost + costs[i] <= budget:
            selected.append(i)

            total_cost += costs[i]
            total_influence += influences[i]

    return total_influence, selected


budget = 50

costs = [10, 20, 30]
influences = [60, 100, 120]

exact_influence, exact_selected = maximize_reach(
    budget,
    costs,
    influences
)

greedy_influence, greedy_selected = fast_alternative_strategy(
    budget,
    costs,
    influences
)

print("Exact DP:")
print("Influence:", exact_influence)
print("Selected Users:", exact_selected)
print(
    "Within Budget:",
    is_within_budget(exact_selected, costs, budget)
)

print()

print("Greedy:")
print("Influence:", greedy_influence)
print("Selected Users:", greedy_selected)
print(
    "Within Budget:",
    is_within_budget(greedy_selected, costs, budget)
)