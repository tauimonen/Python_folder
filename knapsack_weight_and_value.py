"""Solution for knapsack problem (weight and value)."""

def knapcack(capacity, weights, values):
    """
    Returns the maximum value that can be in given capacity.
    params: int, int-list x 2
    return: int
    """
    n = len(weights)
    table = [[0] * (capacity+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(capacity+1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif weights[i-1] <= j:
                table[i][j] = max(values[i-1] + table[i-1][j-weights[i-1]], table[i-1][j])
            else:
                table[i][j] = table[i-1][j]

    return table[n][capacity]


# test code
capacity = 50
weights = [10, 20, 30]
values = [60, 100, 120]
print(knapcack(capacity, weights, values))