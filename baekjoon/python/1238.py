#1238

import sys
import heapq
input = sys.stdin.readline
INF = int(10**6)

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))

dp = [0 for _ in range(N+1)]

def toparty(start):
    global dp
    distance = [INF for _ in range(N+1)]
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            nxt = i[0]
            cost = dist + i[1]
            if cost < distance[nxt]:
                distance[nxt] = cost
                heapq.heappush(q, (cost, nxt))
    dp[start] = distance[X]

def tohome(X):
    global dp
    distance = [INF for _ in range(N+1)]
    distance[X] = 0
    q = []
    heapq.heappush(q, (0, X))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            nxt = i[0]
            cost = dist + i[1]
            if cost < distance[nxt]:
                distance[nxt] = cost
                heapq.heappush(q, (cost, nxt))
    for i in range(1, N+1):
        dp[i] = dp[i] + distance[i]

for i in range(1, N+1):
    toparty(i)
tohome(X)
print(max(dp))


