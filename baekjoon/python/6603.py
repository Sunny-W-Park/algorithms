#6603

import sys
from __future__ import print_function
from itertools import combinations
input = sys.stdin.readline

while True:
    F = list(map(int, input().split()))
    if F[0] == 0:
        break
    else:
        S = F[1:]
        for j in combinations(S, 6):
            for k in j:
                print(k, end=" ")
            print()
    print()


