#2231

input = sys.stdin.readline
N = int(input())
result = []

a = 0

def function(a):
    num = a
    for i in range(len(str(a))):
        num += int(str(a)[i])
    return num

while a <= N:
    a += 1
    if function(a) == N:
        result.append(a)
        break

if len(result) == 0:
    print(0)
else:
    print(result[0])

#2798

input = sys.stdin.readline
a, b = map(int, input().split())
arr = list(map(int, input().split()))
result = []

for i in range(a):
    for j in range(a):
        for k in range(a):
            num = arr[i] + arr[j] + arr[k]
            if i != j and j != k and i!= k and num <= b:
                result.append(num)

print(sorted(result)[-1])

#1018 "재풀이(1)"

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]

count = []

for i in range(N - 7):
    for j in range(M - 7):
        count_w, count_b = 0, 0
        for p in range(i, i + 8):
            for q in range(j, j + 8):
                if (p + q) % 2 == 0:
                    if arr[p][q] != 'W':
                        count_w += 1
                    if arr[p][q] != 'B':
                        count_b += 1
                elif (p + q) % 2 == 1:
                    if arr[p][q] != 'B':
                        count_w += 1
                    if arr[p][q] != 'W':
                        count_b += 1
        count.append(count_w)
        count.append(count_b)

print(min(count))

