#Combination

N, M = map(int, input().split())

count = 0
result = [0 for _ in range(N+1)]

def dfs(length, idx):
    global count
    if length == M:
        for i in range(M):
            print(result[i], end = ' ')
        print()
        count += 1
    else:
        for i in range(idx, N+1):
            result[length] = i
            dfs(length+1, i+1)

dfs(0, 1)

