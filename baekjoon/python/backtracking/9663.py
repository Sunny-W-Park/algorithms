#9663


#9663 재풀이 - check 조건 통일


#9663 재풀이 - 풀이과정 참고 

import sys
input = sys.stdin.readline
N = int(input())

row = [0] * N
visited = [0] * N
count = 0

def check(q):
    for i in range(q):
        if abs(row[q] - row[i]) == (q - i):
            return False
    return True

def dfs(q):
    global count
    if q == N:
        count += 1
        return
    for i in range(N):
        if visited[i] == 1:
            continue
        ##
        row[q] = i
        if check(q) == True:
            visited[i] = 1
            dfs(q+1)
            visited[i] = 0

dfs(0)
print(count)

#9663 1차 풀이

import sys
import time

N = int(input())
p = []
ans = 0

def dfs():
    global ans
    if len(p) == N:
        ans += 1
        return
    else:
        for i in range(N):
            for j in range(N):
                if len(p) > 0:
                    if i < p[-1][0]:
                        continue
                avab = True
                for k in p:
                    if i == k[0] or j == k[1]:
                        avab = False
                        continue
                    if abs(i-k[0]) == abs(j-k[1]):
                        avab = False
                        continue
                if avab == True:
                    p.append((i, j))
                    dfs()
                    p.pop()

start = time.time()
dfs()
print(ans)
print("time: ", time.time() - start)


