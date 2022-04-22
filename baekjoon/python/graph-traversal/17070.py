#17070

N = int(input())
g = []
for _ in range(N):
    g.append(list(map(int, input().split())))

count = 0

def dfs(x, y, status):
    global count
    if x == N-1 and y == N-1:
        count += 1

    if status == 'h':
        if (y+1) <= N-1:
            if g[x][y+1] == 0:
                dfs(x, y+1, 'h')
        if (x+1) <= N-1 and (y+1) <= N-1:
            if g[x+1][y] == 0 and g[x][y+1] == 0 and g[x+1][y+1] == 0:
                dfs(x+1, y+1, 'd')

    if status == 'v':
        if (x+1) <= N-1:
            if g[x+1][y] == 0:
                dfs(x+1, y, 'v')
        if (x+1) <= N-1 and (y+1) <= N-1:
            if g[x+1][y] == 0 and g[x][y+1] == 0 and g[x+1][y+1] == 0:
                dfs(x+1, y+1, 'd')
    
    if status == 'd':
        if (y+1) <= N-1:
            if g[x][y+1] == 0:
                dfs(x, y+1, 'h')
        if (x+1) <= N-1:
            if g[x+1][y] == 0:
                dfs(x+1, y, 'v')
        if (x+1) <= N-1 and (y+1) <= N-1:
            if g[x+1][y] == 0 and g[x][y+1] == 0 and g[x+1][y+1] == 0:
                dfs(x+1, y+1, 'd')
    
dfs(0, 1, 'h')
print(count)
