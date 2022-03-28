#15686

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

houses = []
chicken = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            houses.append((i, j))
        if graph[i][j] == 2:
            chicken.append((i, j))

chicken_distance = []
for i in chicken:
    d = 0
    for j in houses:
         d += (abs(i[0]-j[0]) + abs(i[1]-j[1]))
    chicken_distance.append((d, i[0], i[1]))
chicken_distance.sort()
chicken_distance = chicken_distance[0:M]

result = 0
for i in houses:
    _min = int(10**9)
    for j in chicken_distance:
        _min = min(_min, (abs(i[0]-j[1])+abs(i[1]-j[2])))
    result += _min

print(result)


