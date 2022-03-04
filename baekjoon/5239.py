#5239

import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    c = list(map(int, input().split()))
    x = [0 for _ in range(9)]
    y = [0 for _ in range(9)]

    for i in range(1, len(c)-1, 2):
        x[c[i]] += 1

    for j in range(2, len(c), 2):
        y[c[j]] += 1

    SAFE = True

    for k in range(9):
        if x[k] > 1 or y[k] > 1:
            SAFE = False
            break

    if SAFE == True:
        print("SAFE")
    else:
        print("NOT SAFE")

