#Floyd-Warshall algorithm

#알고리즘 원리: 모든 노드에서 다른모든 노드까지의 최단경로

INF = int(1e9)

N, M = map(int, input().split()) #노드, 간선의 개수
graph = [[INF for _ in range(N+1)] for _ in range(N+1)] #2차원 최단거리 그래프

#자기 자신으로 가는 비용 0으로 초기화
for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

#각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c

#점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i!=j and i!=k and j!=k:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

#결과 출력
for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == INF:
            print("INF", end = " ")
        else:
            print(graph[i][j], end = " ")
    print()


