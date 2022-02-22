#1913

import sys
input = sys.stdin.readline
N = int(input())
T = int(input())

g = [[0 for _ in range(N)] for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
g[0][0] = N**2

p = N-1 #x
q = N-1 #y
d = 0
x = 0
y = 0

while True:
    if g[x][y] == 1:
        break
    else:
        nx = x + dx[d]
        ny = y + dy[d]
        if N-1-p <= nx <= p and N-1-q <= ny <= q:
            g[nx][ny] = g[x][y] - 1
            x, y = nx, ny
        else:
            d += 1
            if d == 3:
                q -= 1
            if d == 4:
                d = 0
                p -= 1

a = 0
b = 0
for i in range(N):
    for j in range(N):
        if g[i][j] == T:
            a = i
            b = j
        print(g[i][j], end = " ")
    print()
print(a+1, b+1)

