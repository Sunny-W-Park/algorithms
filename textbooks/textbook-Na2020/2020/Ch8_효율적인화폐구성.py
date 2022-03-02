#오답제출

N, M = map(int, input().split())
arr = [0 for i in range(N)]
for i in range(N):
    arr[i] = int(input())

d = [0] * (M + 1)

for i in range(N):
    for j in range(arr[i], M+1):
        d[j] = min(d[j], d[j - arr[i]] + 1)

if d[M] == 0:
    print(-1)
else:
    print(d[M])
