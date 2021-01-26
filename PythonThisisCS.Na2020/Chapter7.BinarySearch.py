import sys
sys.setrecursionlimit(10**6)


#부품 찾기 - 반복문

N = int(input())
arr1 = list(map(int, (input().split())))

M = int(input())
arr2 = list(map(int, (input().split())))

result = []

for i in range(M):
        if arr2[i] in arr1:
            result.append("Yes")
        else:
            result.append("No")

for k in range(len(result)):
    print(result[k], end = ' ')

#부품 찾기 - 이진탐색

N = int(input())
arr1 = sorted(list(map(int, (input().split()))))

M = int(input())
arr2 = list(map(int, (input().split())))

result = []

def binary_search(array, target, start, end):
    mid = (start + end) // 2
    if start > end:
        return result.append("No")
    #위치? 아래에 있으면 안되는 이유

    if array[mid] == target:
        return result.append("Yes")

    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)

    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)

array = arr1
for i in range(M):
    target = arr2[i]
    start, end = 0, N-1
    binary_search(array, target, start, end)
    print(result[i], end = ' ')


