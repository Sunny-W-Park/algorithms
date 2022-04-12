
#10815

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

result = [0 for _ in range(20000001)]

for i in nums:
    result[i+10000000] = 1

for j in targets:
    if result[j+10000000] == 1:
        print(1, end = ' ')
    else:
        print(0, end = ' ')

