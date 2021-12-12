#2739

n = int(input())

for i in range(1, 10):
    print("%d * %d = %d" % (n, i, n * i))

#10960

t = int(input())
list = []

for i in range(t):
    a, b = map(int, input().split())
    list.append(a + b)

for j in range(t):
    print(list[j])

#8393

n = int(input())

sum = 0

for i in range(1, n+1):
    sum += i

print(sum)

