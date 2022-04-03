#C

import sys
import bisect
import math
from itertools import combinations
input = sys.stdin.readline

N = int(input())
S = input()
W = []
H = []
E = []
for i in range(len(S)):
    if S[i] == 'W':
        W.append(i)
    if S[i] == 'H':
        H.append(i)
    if S[i] == 'E':
        E.append(i)

result = 0
for i in H:
    for j in W:
        if i > j:
            pos = bisect.bisect_left(E, i)
            E_copy = E[pos:]
            if len(E_copy) >= 2:
                for k in range(2, len(E_copy)+1):
                    result += math.factorial(len(E_copy)) // (math.factorial(k) * math.factorial(len(E_copy)-k))

print(result%1000000007)

#A

import sys
import copy
from itertools import permutations

input = sys.stdin.readline
N = int(input())
price = list(map(int, input().split()))
discounts = [[] for _ in range(N)]
for i in range(N):
    t = int(input())
    for j in range(t):
        a, d = map(int, input().split())
        discounts[i].append((a, d))

_min = int(10**9)
base = [i for i in range(1, N+1)]

for i in permutations(base):
    result = 0
    price_copy = copy.copy(price)
    for k in range(len(i)):
        result += price_copy[i[k]-1]
        for p in discounts[i[k]-1]:
            if price_copy[p[0]-1] - p[1] > 0:
                price_copy[p[0]-1] = price_copy[p[0]-1] - p[1]
            else:
                price_copy[p[0]-1] = 1
    _min = min(_min, result)


print(_min)
