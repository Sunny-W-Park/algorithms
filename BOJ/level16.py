#11047

input = sys.stdin.readline
N, K = map(int, input().split())
coins = []
for i in range(N):
    coins.append(int(input()))

count = 0
start_index = N - 1

while True:
    if K == 0:
        print(count)
        break
    else:
        if K - coins[start_index] >= 0:
            K = K - coins[start_index]
            count += 1
        else:
            start_index = start_index - 1

#11399

input = sys.stdin.readline
N = int(input())
P = list(map(int, input().split()))
P = sorted(P)

print(P)

Total = 0

for i in range(N):
    count = 0
    for j in range(i+1):
        count += P[j]
    Total += count

print(Total)

