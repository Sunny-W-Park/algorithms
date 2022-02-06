#10773

import sys
input = sys.stdin.readline

K = int(input())
arr = []
for _ in range(K):
    x = int(input())
    if x == 0:
        arr.pop()
    else:
        arr.append(x)

print(sum(arr))


