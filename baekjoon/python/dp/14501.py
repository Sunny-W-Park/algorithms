#14501 재풀이

N = int(input())

table = []
for _ in range(N):
    t, p = map(int, input().split())
    table.append([t, p])

dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    if i + table[i][0] -1 > N-1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i+table[i][0]]+table[i][1])

print(max(dp))


