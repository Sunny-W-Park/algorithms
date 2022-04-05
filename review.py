#2022.04.01

#11000 우선순위큐

import sys
import heapq
input = sys.stdin.readline
N = int(input())

classes = []
for _ in range(N):
    start, end = map(int, input().split())
    classes.append((start, end))
classes.sort()

room = []
heapq.heappush(room, classes[0][1])

for i in range(1, N):
    if classes[i][0] < room[0]:
        heapq.heappush(room, classes[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, classes[i][1])

print(len(room))


#2022.03.08

#17265 DFS

#17265 재풀이

import sys
input = sys.stdin.readline
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(str, input().split())))

dx = [1, 0]
dy = [0, 1]

mv = -(5**25)
nv = 5**25
ops = ["+", "-", "*"]

def dfs(x, y, before, operator):
    global mv
    global nv
    for k in range(2):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx <= N-1 and 0 <= ny <= N-1:
            if graph[nx][ny] in ops:
                dfs(nx, ny, before, graph[nx][ny])
            else:
                if operator == '+':
                    dfs(nx, ny, int(before) + int(graph[nx][ny]), '')
                if operator == '-':
                    dfs(nx, ny, int(before) - int(graph[nx][ny]), '')
                if operator == '*':
                    dfs(nx, ny, int(before) * int(graph[nx][ny]), '')
        if nx == N-1 and ny == N-1:
            fv = 0
            if operator == '+':
                fv = int(before) + int(graph[nx][ny])
            if operator == '-':
                fv = int(before) - int(graph[nx][ny])
            if operator == '*':
                fv = int(before) * int(graph[nx][ny])
            mv = max(mv, fv)
            nv = min(nv, fv)

dfs(0, 0, int(graph[0][0]), '')
print(mv, nv)

#2022.03.04

#2293 DP

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
dp = [0 for _ in range(k+1)]
dp[0] = 1

for coin in coins:
    for j in range(coin, k+1):
        dp[j] += dp[j-coin]

print(dp[k])

#2022.02.28

#11053 LIS 재풀이: DP

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))

#12015 LIS 재풀이: 이분탐색

import sys
import bisect
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

arr = [0]

for i in A:
    if arr[-1] < i:
        arr.append(i)
    else:
        arr[bisect.bisect_left(arr, i)] = i

print(len(arr)-1)

#2022.02.20

#11403 재풀이

N = int(input())
g = []
for _ in range(N):
    g.append(list(map(int, input().split())))

def dfs(i):
    for j in range(N):
        if visited[j] == 0 and g[i][j] == 1:
            visited[j] = 1
            dfs(j)

visited = [0 for _ in range(N)]
for i in range(N):
    dfs(i)
    for j in range(N):
        if visited[j] == 1:
            print(1, end = " ")
        if visited[j] == 0:
            print(0, end = " ")
    print()
    visited = [0 for _ in range(N)]

#2022.02.18

#2178 BFS로 풀기

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph_line = []
graph = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(N):
    graph_line.append(str(input()))
for i in range(N):
    for j in range(M):
        graph[i][j] = int(graph_line[i][j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

start_x, start_y = 0, 0
q = deque([start_x, start_y])

while len(q) != 0:
    pos_x = q.popleft()
    pos_y = q.popleft()
    for i in range(4):
        nx = pos_x + dx[i]
        ny = pos_y + dy[i]
        if 0 <= nx <= N-1 and 0 <= ny <= M-1:
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[pos_x][pos_y] + 1
                q.append(nx)
                q.append(ny)

print(graph[N-1][M-1])

#2022.02.10

#11052

import sys
input = sys.stdin.readline

N = int(input())
B = list(map(int, input().split()))
C = [0]
for i in range(N):
    C.append(B[i])
dp = [0 for _ in range(N+1)]

dp[1] = C[1]

for i in range(2, N+1):
    for j in range(1, i+1):
        if dp[i] < dp[i-j] + C[j]:
            dp[i] = dp[i-j] + C[j]
print(dp[N])

#2156

import sys
input = sys.stdin.readline

N = int(input())
W = [0]
for i in range(N):
    W.append(int(input()))
dp = [0]
dp.append(W[1])

if N > 1:
    dp.append(W[1] + W[2])

for i in range(3, N+1):
    dp.append(max(dp[i-1], dp[i-3] + W[i-1] + W[i], dp[i-2] + W[i]))

print(dp[N])

#2156

import sys
input = sys.stdin.readline

N = int(input())
W = [0 for _ in range(10001)]
for i in range(1, N):
    W[i] = int(input())
dp = [0 for _ in range(10001)]

dp[1] = W[1]
dp[2] = W[1] + W[2]

for i in range(3, N+1):
    dp[i] = max(dp[i-2] + W[i], dp[i-3] + W[i-1] + W[i], dp[i-1])

print(dp[N])

#2022.01.28

#1300 풀이과정 참고

import sys

N = int(input())
K = int(input())
start, end = 1, K

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in range(1, N+1):
        count += min(N, mid//i)

    if count < K:
        start = mid + 1
    elif count >= K:
        end = mid - 1

print(start)

#2110 풀이과정 참고

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

#2022.01.27

#2805

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums = sorted(nums)

start = 0
end = nums[-1]
arr = []

while start <= end:
    result = 0
    mid = (start + end) // 2
    for i in nums:
        if i > mid:
            result += i - mid
    if result >= M:
        arr.append(mid)
        start = mid + 1
    else:
        end = mid - 1

print(arr[-1])

#2022.01.25

#1715

import heapq

N = int(input())

cards = []
for _ in range(N):
    cards.append(int(input()))
heapq.heapify(cards)
result = 0

while len(cards) != 1:
    num1 = heapq.heappop(cards)
    num2 = heapq.heappop(cards)
    add = num1 + num2
    result += add
    heapq.heappush(cards, add)

print(result)

#2022.01.19

#2004 재풀이

input = sys.stdin.readline
n, m = map(int, input().split())

def count(n, k):
    count = 0
    while n > 1:
        n = n // k
        count += n
    return count

count_five = count(n, 5) - (count(n - m, 5) + count(m, 5))
count_two = count(n, 2) - (count(n - m, 2) + count(m, 2))
print(min(count_two, count_five))

#2022.01.18

#9375

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n = int(input())

    #n이 0인 경우 건너뛰기
    if n == 0:
        print(0)
        continue

    items = dict()
    for _ in range(n):
        a, b = map(str, input().split())
        if b in items.keys():
            items[b] += 1
        #dictionary 데이터 추가 방법
        else:
            items[b] = 1

        answer = 1
        for key in items.keys():
            answer *= (items[key] + 1)

    #안입는 경우 제외
    print(answer - 1)

#1934 재풀이

input = sys.stdin.readline
N = int(input())

def lcd(A, B):
    if B == 0:
        return A
    else:
        return lcd(B, A % B)

def gcm(A, B):
    return (A * B) // lcd(A, B)

for _ in range(N):
    A, B = map(int, input().split())
    print(gcm(A, B))

#2022.01.10

#백트래킹(DFS)

#15650

sys.setrecursionlimit(10000)

input = sys.stdin.readline
N, M = map(int, input().split())
s = []

def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(1, N + 1):
        if i in s:
            continue
        s.append(i)
        dfs()
        s.pop()

dfs()

#2022.01.09

#1018 "재풀이(1)"

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]

count = []

for i in range(N - 7):
    for j in range(M - 7):
        count_w, count_b = 0, 0
        for p in range(i, i + 8):
            for q in range(j, j + 8):
                if (p + q) % 2 == 0:
                    if arr[p][q] != 'W':
                        count_w += 1
                    if arr[p][q] != 'B':
                        count_b += 1
                elif (p + q) % 2 == 1:
                    if arr[p][q] != 'B':
                        count_w += 1
                    if arr[p][q] != 'W':
                        count_b += 1
        count.append(count_w)
        count.append(count_b)

print(min(count))

#2022.01.07

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

#2022.01.05

#10989

n = int(input())

check_list = [0 for _ in range(10000)]

for i in range(n):
    num = int(input())
    check_list[num - 1] = check_list[num - 1] + 1

for i in range(len(check_list)):
    if check_list[i] != 0:
        for j in range(check_list[i]):
            print(i + 1)        #해당 index(i+1)를 횟수(j) 만큼 출력

#2021.12.16

#11729

n = int(input())
list = []

def hanoi(n, x, y):
    global list
    if n > 1:
        hanoi(n - 1, x, 6 - x - y)

    list.append([x, y])

    if n > 1:
        hanoi(n - 1, 6 - x - y, y)

hanoi(n, 1, 3)
print(len(list))
for i in range(len(list)):
    print(list[i][0], list[i][1])

#1002

t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(float, input().split())
    d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

    if d == 0 and r1 == r2:
        print(-1)

    elif r1 + r2 == d or abs(r1 - r2) == d:
        print(1)

    elif abs(r1 - r2) < d < r1 + r2:
        print(2)

    else:
        print(0)

#4673

natural_num = set(range(1, 10001))
generated_num = set()
#set 자료형의 특징
#1) 순서 없음 -> sort로 정렬 필요
#2) 중복 없음 -> 데이터 입력시 중복을 차단해주는 역할 수행

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generated_num.add(i)

result_num = sorted(natural_num - generated_num)

for k in result_num:
    print(k)

#2021.12.28 

#9020

def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

numbers = list(range(2, 10001))
prime = []
for i in numbers:
    if isPrime(i):
        prime.append(i)

t = int(input())

for i in range(t):
    n = int(input())
    a = 0
    b = 0
    for j in range(len(prime)):
        if prime[j] >= n/2:         ##2로 나눈 중간값부터 탐색(두 소수의 차이가 가장 작은 것)
            if n - prime[j] in prime:       ## "in prime" 으로 다른 수 탐색
                b = prime[j]
                a = n - prime[j]
                break       ##break를 통해 j가 range의 끝까지 탐색하는 것을 방지
    print(a, b)

