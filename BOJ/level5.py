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

