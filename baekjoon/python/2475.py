#2475

import sys

arr = list(map(int, input().split()))
result = 0
for i in range(len(arr)):
    result += arr[i] ** 2

print(result % 10)


