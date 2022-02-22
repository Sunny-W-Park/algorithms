#Djikstra shortest path

#알고리즘 원리: 출발 노드에서 다른 모든 노드까지 가는 최단경로
#1. 출발 노드 설정
#2. 최단 거리 테이블 초기화
#3. 방문하지 않은 노드 중 최단거리가 가장 짧은 노드 선택
#4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
#5. 위 과정에서 #3과 #4의 과정 반복

#방법1. 간단한 다익스트라 알고리즘

import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split()) #노드, 간선 개수
start = int(input()) #시작 노드 설정
graph = [[] for _ in range(N+1)] #그래프 생성
visited = [0 for _ in range(N+1)] #노드 방문 여부 확인용 리스트
distance = [INF for _ in range(N+1)] #최단거리 테이블 초기화

#노드/간선/가중치 정보 저장
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) #튜플 형태로 저장 

#방문하지 않은 노드 중, 최단거리가 가장 짧은 노드의 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, N+1):
        if distance[i] < min_value and visited[i] == 0:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = 1
    for i in graph[start]:
        distance[i[0]] = i[1]
    #시작노드를 제외하고 get_smallest_node 반복
    for i in range(N-1):
        now = get_smallest_node
        visited[now] = 1
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

#뱡법2. 개선된 다익스트라 알고리즘

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
start = int(input())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))





