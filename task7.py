import random

analytical_probabilities = {
    2: (1 / 36) * 100,
    3: (2 / 36) * 100,
    4: (3 / 36) * 100,
    5: (4 / 36) * 100,
    6: (5 / 36) * 100,
    7: (6 / 36) * 100,
    8: (5 / 36) * 100,
    9: (4 / 36) * 100,
    10: (3 / 36) * 100,
    11: (2 / 36) * 100,
    12: (1 / 36) * 100,
}

# Monte Carlo simulatio
def monte_carlo_dice_simulation(num_rolls):
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        roll_sum = dice1 + dice2
        sums_count[roll_sum] += 1

    simulated_probabilities = {roll: (count / num_rolls) * 100 for roll, count in sums_count.items()}

    return simulated_probabilities

# run
num_rolls = 1000000
simulated_probabilities = monte_carlo_dice_simulation(num_rolls)

print("Sum | Simulated Probability (%) | Analytical Probability (%)")
print("----|---------------------------|----------------------------")
for sum_value in range(2, 13):
    print(f"{sum_value:>3} | {simulated_probabilities[sum_value]:>24.2f}% | {analytical_probabilities[sum_value]:>25.2f}%")