#10810

n = int(input())
ints = list(map(int, sys.stdin.readline().split()))

min = ints[0]
max = ints[0]

for i in range(n):
    if ints[i] < min:
        min = ints[i]

for j in range(n):
    if ints[j] > max:
        max = ints[j]

print(min, max)

#2562

list = []

for i in range(9):
    list.append(int(sys.stdin.readline()))

max = list[0]
index = 0

for j in range(9):
    if list[j] > max:
        max = list[j]
        index = j+1
    elif list[j] == max:
        index = j+1

print(max)
print(index)

#2577

list = []

for i in range(3):
    list.append(int(sys.stdin.readline()))

result = [str(list[0] * list[1] * list[2])]

count = [0 for x in range(10)]

for m in range(len(result[0])):
    for n in range(10):
        if result[0][m] == str(n):
            count[n] += 1

for k in range(10):
    print(count[k])


#3052

list = []

for i in range(10):
    list.append(int(sys.stdin.readline()) % 42)

result = [1 for _ in range(10)]

for j in range(10):
    for k in range(10):
        if j != k:
            if list[j] == list[k]:
                result[j] = 0

        elif j == k:
            if list[j] == list[k]:
                result[j] = 1

print(sum(result))

#1546

n = int(input())

list = list(map(int, sys.stdin.readline().split()))

max = list[0]

for i in range(n):
    if list[i] > max:
        max = list[i]

result = []

for j in range(n):
    result.append(list[j] / max * 100)

print(sum(result) / n)

#8958

n = int(input())
list = []

for i in range(n):
    list.append(str(input()))

count = []

for j in range(n):
    count.append([0 for k in range(len(list[j]))])

for p in range(n):
    for q in range(len(list[p])):
        if list[p][q] == 'O':
            count[p][q] = 1

for p in range(n):
    for q in range(len(count[p])):
        if q >= 1:
            if count[p][q] >= 1 and count[p][q-1] >= 1:
                count[p][q] = count[p][q-1] + 1

for x in range(n):
    print(sum(count[x]))

#4344

n = int(input())
arr = [0 for _ in range(n)]

for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().split()))

avg = [0 for _ in range(n)]

for j in range(n):
    avg[j] = (sum(arr[j]) - arr[j][0]) / arr[j][0]

count = [0 for _ in range(n)]

for p in range(n):
    for q in range(arr[p][0]+1):
        if q >= 1:
            if arr[p][q] > avg[p]:
                count[p] += 1

for x in range(n):
    count[x] = float((count[x] / arr[x][0]) * 100)
    print('{:.3f}%'.format(count[x]))

