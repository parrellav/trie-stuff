def knap_sack(profits, profits_length, weights, capacity):
    """
    Finds the maximum value that can be put in a knapsack
    :param profits: The profit that can be gained by each item
    :param profits_length: The number of pieces of jewelry
    :param weights: The weight of each piece of jewelry
    :param capacity: The maximum weight that the knapsack can hold
    :return: Maximum value that can be put in a knapsack
    """
    total_profit = 0
    remaining_capacity = capacity
    for i in range(profits_length - 1, 0, -1):
        profit = profits[i]
        weight = weights[i]
        if remaining_capacity >= weight:
            total_profit += profit
            remaining_capacity -= weight
    return total_profit