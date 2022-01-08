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

