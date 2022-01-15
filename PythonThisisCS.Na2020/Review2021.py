#예제 3-1. 거스름돈

coins = [10, 50, 100, 500]
N = int(input())
count = 0

index = len(coins)-1
while index >= 0:
    if N - coins[index] >= 0:
        N -= coins[index]
        count += 1
    elif N - coins[index] < 0:
        index -= 1
    if N == 0:
        break

print(count)

#답안

coins = [500, 100, 50, 10]
N = int(input())
count = 0

for i in coins:
    count += N // i
    n %= i

#예제 3-2. 큰 수의 법칙

input = sys.stdin.readline
N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
arr_sorted = sorted(arr, reverse = True)

result = 0
count = 0
index = 0
index_count = 0

while count != M:
    if index_count < K:
        result += arr_sorted[index]
        index_count += 1
        count += 1
    elif index_count == K:
        index += 1
        index_count = 0
        result += arr_sorted[index]
        count += 1
        index = 0

print(result)

#예제 3-3. 숫자 카드 게임

input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
mins = []

for i in range(N):
    data = list(map(int, input().split()))
    arr.append(data)
    mins.append(min(data))

index = 0
for i in range(N):
    if mins[i] == max(mins):
        index = i

print(min(arr[index]))

#예제 3-4. 1이 될 때까지

input = sys.stdin.readline
N, K = map(int, input().split())

count = 0
while N != 1:
    if N % K == 0:
        N = N / K
        count += 1
    else:
        N = N - 1
        count += 1

print(count)


