#2559

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = K-1
S = sum(arr[start:end+1])
result = S 

while end < N-1:
    S -= arr[start]
    start += 1
    end += 1
    S += arr[end]
    result = max(result, S)

print(result)
