"""
Find the longest ascending substring in random order numbers 1,2,…, n
"""

import random

n = 5000
taulu = list(range(1, n))
random.shuffle(taulu)
pisin = [0] * (n + 1)

for i in range(0, n - 1):
    pisin[i] = 1
    for j in range(0, i - 1):
        if taulu[j] < taulu[i] and pisin[j] + 1 > pisin[i]:
            pisin[i] = pisin[j] + 1

pisin_nouseva_alijono = max(pisin)
print(pisin_nouseva_alijono)