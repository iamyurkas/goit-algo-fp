items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, value in sorted_items:
        if total_cost + value['cost'] <= budget:
            selected_items.append(item)
            total_cost += value['cost']
            total_calories += value['calories']

    return selected_items, total_calories, total_cost


def dynamic_programming(items, budget):
    item_names = list(items.keys())
    n = len(item_names)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item = items[item_names[i - 1]]
        for b in range(budget + 1):
            if item['cost'] <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - item['cost']] + item['calories'])
            else:
                dp[i][b] = dp[i - 1][b]

    selected_items = []
    total_calories = dp[n][budget]
    b = budget

    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            selected_items.append(item_names[i - 1])
            b -= items[item_names[i - 1]]['cost']

    selected_items.reverse()

    total_cost = sum(items[item]['cost'] for item in selected_items)

    return selected_items, total_calories, total_cost


# usage
budget = 100

selected_greedy, calories_greedy, cost_greedy = greedy_algorithm(items, budget)
print("Greedy Algorithm:")
print("Selected Items:", selected_greedy)
print("Total Calories:", calories_greedy)
print("Total Cost:", cost_greedy)

selected_dp, calories_dp, cost_dp = dynamic_programming(items, budget)
print("\nDynamic Programming:")
print("Selected Items:", selected_dp)
print("Total Calories:", calories_dp)
print("Total Cost:", cost_dp)