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

