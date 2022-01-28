#1920

import sys

input = sys.stdin.readline
N = int(input())
list_N = list(map(int, input().split()))
list_N = sorted(list_N)
M = int(input())
list_M = list(map(int, input().split()))

def binary_search(data, start, target, end):
    if start > end:
        print(0)
        return None
    mid = (start + end) // 2
    if data[mid] == target:
        print(1)
    if data[mid] > target:
        binary_search(data, start, target, mid-1)
    if data[mid] < target:
        binary_search(data, mid+1, target, end)

for i in list_M:
    binary_search(list_N, 0, i, N-1)


#10816 bisect 내장함수 활용

from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
nums = sorted(nums)
M = int(input())
targets = list(map(int, input().split()))

print(nums)
print(targets)

def binary_search(data, left, right):
    right_index = bisect_right(data, right)
    left_index = bisect_left(data, left)
    print(right_index, left_index)

for i in range(len(targets)):
    binary_search(nums, targets[i], targets[i])

#10816 시간초과

import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
nums = sorted(nums)
M = int(input())
targets = list(map(int, input().split()))
results = []

def binary_search(data, target):
    start = 0
    end = N-1
    count = 0
    k = 0
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            k = mid
            break
        elif data[mid] > target:
            end = mid - 1
        elif data[mid] < target:
            start = mid + 1

    for i in range(k, N):
        if data[i] == target:
            count += 1
        else:
            break
    for j in range(k-1, -1, -1):
        if data[j] == target:
            count += 1
            break

    print(count, end = ' ')

for i in targets:
    binary_search(nums, i)

#2805 풀이과정 참고

import sys

input = sys.stdin.readline
N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))
houses.sort()

start = 1
end = houses[-1]
ans = 0

while start <= end:
    mid = (start + end) // 2
    count = 1
    pos = houses[0]
    d = float("INF")

    for i in range(1, N):
        if pos + mid <= houses[i]:
            d = min(houses[i]-pos, d)
            count += 1
            pos = houses[i]

    if count < C:
        end = mid - 1

    elif count >= C:
        start = mid + 1
        ans = max(ans, d)

print(ans)


