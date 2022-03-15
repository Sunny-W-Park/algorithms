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


#1541 '괄호 수 제한 없는 경우'

s = str(input())
numbers = []
operators = []
put = ''

for i in range(len(s)):
    if s[i] == '+' or s[i] == '-':
        operators.append(s[i])
        numbers.append(put)
        put = s[i]
    else:
        put += s[i]
    if i == len(s)-1:
        numbers.append(put)

converter = 1

for i in range(len(numbers)):
    if int(numbers[i]) < 0:
        converter = -1
    if converter == 1:
        numbers[i] = int(numbers[i])
    if converter == -1:
        if int(numbers[i]) > 0:
            numbers[i] = -1 * int(numbers[i])
        else:
            numbers[i] = int(numbers[i])

print(sum(numbers))

#13305

input = sys.stdin.readline

N = int(input())
distance = list(map(int, input().split()))
oilprice = list(map(int, input().split()))

result = 0
charger = oilprice[0]

for i in range(len(oilprice)-1):
    if charger <= oilprice[i]:
        result += charger * distance[i]
    else:
        charger = oilprice[i]
        result += charger * distance[i]

print(result)

#1931 2차 풀이

input = sys.stdin.readline
N = int(input())
arr = []

for i in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])

arr.sort(key = lambda x: x[0])
arr.sort(key = lambda x: x[1])

count = 1
end_time = arr[0][1]

for i in range(1, N):
    if arr[i][0] >= end_time:
        count += 1
        end_time = arr[i][1]

print(count)

