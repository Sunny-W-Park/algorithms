#1466

n, m = map(int, input().split())
arr = [[0 for i in range(m)] for j in range(n)]
newarr = [[0 for i in range(m)] for j in range(n)]
begin = 1

for k in range(n):
    arr[k][0] = begin + k
    for l in range(m):
        arr[k][l] = arr[k][0] + n*l

for k in range(n):
    arr[k].sort(reverse = True)

for k in range(n):
    newarr[k] = arr[-k-1]
    for l in range(m):
        print(newarr[k][l], end = ' ')
    print()


#1465

n, m = map(int, input().split())
arr = [[0 for i in range(m)] for j in range(n)]
newarr = [[0 for i in range(m)] for j in range(n)]
begin = 0

for k in range(n):
    for l in range(m):
        begin += 1
        arr[k][l] = begin

for k in range(n):
    newarr[k] = arr[-k-1]
    for l in range(m):
        print(newarr[k][l], end = ' ')
    print()


#1464 

n, m = map(int, input().split())
arr = [[0 for i in range(m)] for j in range(n)]
begin = n * m

for k in range(n):
    arr[k][0] = begin - m*k
    for l in range(m):
        arr[k][l] = arr[k][0] - l
        print(arr[k][l], end = ' ')
    print()

#1463

n = int(input())
arr = [[0 for i in range(n)] for j in range(n)]
begin = n

for k in range(n):
    arr[k][0] = begin - k
    for l in range(n):
        arr[k][l] = arr[k][0] + n*l
        print(arr[k][l], end = ' ')
    print()

#1462

n = int(input())
arr = [[ 0 for i in range(n)] for j in range(n)]
begin = 1

for k in range(n):
    arr[k][0] = begin + k
    for l in range(n):
        arr[k][l] = arr[k][0] + n*l
        print(arr[k][l], end = ' ')
    print()


#1461

n = int(input())
arr = [[0 for i in range(n)] for j in range(n)]

for k in range(n):
    for l in range(n):
        arr[k][0] = n * (k+1)
        arr[k][l] = arr[k][0] - l
        print(arr[k][l], end = ' ')
    print()



#1460

n = int(input())
arr = [[0 for i in range(n)] for j in range(n)]
size = n * n
begin = 0 

for i in range(n):
    for j in range(n):
        begin += 1
        arr[i][j] = begin
        print(arr[i][j], end = ' ')
    print()
