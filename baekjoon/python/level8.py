#1712

a, b, c = map(int, input().split())

q = 0

if b >= c:
    q = -1

else:
    q = a // (c-b) + 1

print(q)

#2292

n = int(input())

i = 0
start = 1
end = 1

while True:
    if end >= n >= start:
        print(i+1)
        break
    else:
        i = i+1
        start = end + 1
        end = end + 6 * i

#1193

x = int(input())

index_start = 1
index_end = 1
d = 1

while True:
    if index_end >= x >= index_start:
        break
    else:
        index_start = index_start + d
        d = d + 1
        index_end = index_end + d

index = x - index_start
a = 1
b = d
a = a + index
b = b - index

if d % 2 == 0:
    print(str(a) + "/" + str(b))

else:
    print(str(b) + "/" + str(a))

#2869

import math

a, b, v = map(int, input().split())
x = (v - b) / (a - b)
x_ceil = math.ceil(x)
print(x_ceil)

#10250

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

floor = 0
room = 0
result = []

for i in range(n):
    if arr[i][2] % arr[i][0] == 0:
        floor = arr[i][0]

        if arr[i][2] // arr[i][0] >= 1:
            room = arr[i][2] // arr[i][0]

        elif arr[i][2] // arr[i][0] == 0:
            room = 1

    else:
        if arr[i][2] // arr[i][0] >= 1:
            floor = arr[i][2] % arr[i][0]
            room = arr[i][2] // arr[i][0] + 1

        elif arr[i][2] // arr[i][0] == 0:
            floor = arr[i][2] % arr[i][0]
            room = 1

    if room >= 10:
        result.append(str(floor) + str(room))

    else:
        result.append(str(floor) + '0' + str(room))

for j in range(n):
    print(int(result[j]))

#2775

t = int(input())
kn = [[0 for _ in range(2)] for _ in range(t)]
arr = []

for i in range(t):
    for j in range(2):
        kn[i][j] = int(input())

for i in range(t):
    arr.append([[0 for _ in range(kn[i][1])] for _ in range(kn[i][0]+1)])

for p in range(len(arr)):
    for q in range(len(arr[p][0])):
        arr[p][0][q] = q+1

count = 0

for p in range(len(arr)):
    for q in range(1, len(arr[p])):
        for r in range(len(arr[p][0])):
            count += arr[p][q-1][r]
            arr[p][q][r] = count
        count = 0

for i in range(t):
    print(arr[i][kn[i][0]][kn[i][1]-1])

#2839

n = int(input())

count = 0
result = n

while True:
    if result == 0:
        print(count)
        break

    elif result > 0:
        if result % 5 == 0:
            result = result - 5
            count += 1

        elif (result - 3) % 5 == 0:
            result = result - 3
            count += 1

        elif (result - 5) % 3 == 0:
            result = result - 5
            count += 1

        elif result % 3 == 0:
            result = result - 3
            count += 1

        else:
            result = result - 3
            count += 1

    else:
        print(-1)
        break

#10757

a, b = map(int, input().split())
print(a+b)

#1011

t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    distance = y - x
    result = 1
    n = round(distance ** (1/2))

    if distance == 1:
        result = result

    elif n ** 2 < distance:
        result += 2 * n - 1

    elif n ** 2 >= distance:
        result += 2 * n - 2

    print(result)


