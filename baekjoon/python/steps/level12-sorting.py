import sys


#2750

n = int(input())
list = []

for i in range(n):
    list.append(int(input()))

list.sort()

for i in range(n):
    print(list[i])

#2751

n = int(input())
list = []

for i in range(n):
    list.append(int(input()))

for i in sorted(list):
    print(i)


#10989

n = int(input())

check_list = [0 for _ in range(10001)]

for i in range(n):
    num = int(sys.stdin.readline())
    check_list[num] = check_list[num] + 1

for i in range(10001):
    if check_list[i] != 0:
        for j in range(check_list[i]):
            print(i)        #해당 index(i)를 횟수(j) 만큼 출력

#2108

import sys
input = sys.stdin.readline
N = int(input())
arr = []
dp = [0 for _ in range(8001)]
for _ in range(N):
    x = int(input())
    arr.append(x)
    dp[x+4000] += 1

avg = sum(arr)/N
if avg < 0:
    print(-1 * round(-1 * avg))
else:
    print(round(avg))
print(sorted(arr)[N//2])
mf = []
for i in range(len(dp)):
    if dp[i] == max(dp):
        mf.append(i-4000)
if len(mf) > 1:
    print(sorted(mf)[1])
else:
    print(sorted(mf)[0])
print(max(arr) - min(arr))

#1427

N = str(input())
list = []

for i in range(len(N)):
    list.append(int(N[i]))

list_sorted = sorted(list, reverse = True)

result = ''

for i in range(len(list_sorted)):
    result += str(list_sorted[i])

print(result)

#11650

N = int(input())

arr = []

for i in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])

for i in sorted(arr):
    print(i[0], i[1])

#11651

N = int(input())

arr = []

for i in range(N):
    a, b = map(int, input().split())
    arr.append([b, a])

for i in sorted(arr):
    print(i[1], i[0])

#1181

N = int(input())
arr1 = set()
arr2 = []

for i in range(N):
    word = str(input())
    arr1.add(word)

for i in arr1:
    arr2.append([int(len(i)), i])

for i in sorted(arr2):
    print(i[1])

#10814

N = int(input())
arr = []

for i in range(N):
    a, b = map(str, input().split())
    arr.append([int(a), i, b])

for i in sorted(arr):
    print(i[0], i[2])

#18870

#dict 개념 참고

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr_set_sorted = sorted(set(arr))

dic = {arr_set_sorted[i] : i for i in range(len(arr_set_sorted))}

for i in range(len(arr)):
    print(dic[arr[i]], end = ' ')

#내 풀이

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr_set = set()

for i in range(N):
    arr_set.add(arr[i])

for i in range(N):
    for j in range(len(arr_set)):
        if arr[i] == sorted(arr_set)[j]:
            arr[i] = j
    print(arr[i], end = ' ')




