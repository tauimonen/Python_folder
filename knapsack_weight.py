"""Solving knapsack-problem (weight only) with dynamic
programming."""

def knapsack(T):
    """
    Calculates and returns all the possible weights of
    a list of item weights.
    Param: int list
    return: int
    """
    max_weight = sum(T)
    weights = [False for _ in range(0, max_weight+1)]
    weights[0] = True

    for i in T:
        for j in range(max_weight, -1, -1):
            if weights[j]:
                weights[j + i] = True

    possible_weights = set()
    for i in range(0, max_weight+1):
        if weights[i]:
            possible_weights.add(i)

    return len(possible_weights)


# Test code
T = [1, 3, 3, 4]
print(knapsack(T))