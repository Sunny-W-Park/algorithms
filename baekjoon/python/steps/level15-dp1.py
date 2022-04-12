#1003

#1003 반복문(Bottom-up)

import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n = int(input())
    d = [[0,0] for _ in range(41)]
    d[0][0], d[0][1] = 1, 0
    d[1][0], d[1][1] = 0, 1
    for i in range(2, n+1):
        d[i][0], d[i][1] = d[i-1][0]+d[i-2][0], d[i-1][1]+d[i-2][1]
    print(d[n][0], d[n][1])

#1003 재귀(Top-down)

T = int(input())

def fibo(n):
    global count_zero
    global count_one
    if n == 0:
        count_zero += 1
        return d[0]
    if n == 1:
        count_one += 1
        return d[1]
    else:
        d[n] = fibo(n-1) + fibo(n-2)
        return d[n]

for _ in range(T):
    n = int(input())
    d = [0] * (41)
    d[0], d[1] = 1, 1
    count_zero = 0
    count_one = 0
    fibo(n)
    print(count_zero, count_one)

#9461

import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    d = [0] * 101
    d[0] = 1
    d[1], d[2] = 1, 1
    d[3], d[4] = 2, 2
    n = int(input())
    if n <= 4:
        print(d[n-1])
    else:
        for i in range(5, n+1):
            d[i] = d[i-5] + d[i-1]
        print(d[n-1])

#1149 재풀이

N = int(input())
C = []
for i in range(N):
    C.append(list(map(int, input().split())))
for i in range(1, len(C)):
    C[i][0] = min(C[i-1][1], C[i-1][2]) + C[i][0]
    C[i][1] = min(C[i-1][0], C[i-1][2]) + C[i][1]
    C[i][2] = min(C[i-1][0], C[i-1][1]) + C[i][2]

print(min(C[N-1]))

#1149

import sys
input = sys.stdin.readline

N = int(input())
result = [[3001 for _ in range(3)] for _ in range(N)]
cost = []
for _ in range(N):
    cost.append(list(map(int, input().split())))

for i in range(1, N):
    for j in range(3):
        for k in range(3):
            if j!= k:
                result[i][k] = min(result[i][k], cost[i-1][j] + cost[i][k])

    for q in range(3):
        cost[i][q] = result[i][q]

print(min(result[N-1]))

#1463

import sys
N = int(input())
d = [0] * (N+1)

for i in range(2, N+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1 )
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)

print(d[N])


