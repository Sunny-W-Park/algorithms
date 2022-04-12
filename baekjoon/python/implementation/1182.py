#1182

import sys
from itertools import combinations

input = sys.stdin.readline
N, S = map(int, input().split())
arr = list(map(int, input().split()))

result = []

count = 0

for i in range(1, N+1):
    comb = combinations(arr, i)
    for j in list(comb):
        if sum(j) == S:
            count += 1

print(count)


