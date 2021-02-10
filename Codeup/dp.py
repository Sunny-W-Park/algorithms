#2640
n, k = map(int, input().split())
arr = [0 for i in range(1000000)]

arr[0] = n
for i in range(1, k+1):
    arr[i] = arr[i-1] * n

print(arr[k-1] % 1000000007)

#2602

arr = []
for i in range(3):
    arr.append(list(map(int, input().split())))

newarr = []
for j in range(3):
    newarr.append([arr[0][j], arr[1][j], arr[2][j]])

for k in range(3):
    newarr[k] = sum(newarr[k])

arr.append(newarr)

for l in range(4):
    arr[l].append(sum(arr[l]))

for i in range(4):
    for j in range(4):
        print(arr[i][j], end = ' ')
    print()

#2601 

N = int(input())

arr = [0] * 101
arr[0] = 1
arr[1] = 1

for i in range(2, N):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[N-1])

