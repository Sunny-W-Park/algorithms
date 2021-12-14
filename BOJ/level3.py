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

#15552

t = int(input())
list = []

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    list.append(a+b)

for j in range(t):
    print(list[j])

#2741

n = int(input())

for i in range(1, n+1):
    print(i)

#2742

n = int(input())

result = n

for i in range(0, n):
    result = n - i
    print(result)

#11021

n = int(input())
list = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    list.append(a+b)

for j in range(n):
    print("Case #%d: %d" % (j+1, list[j]))

#11022

n = int(input())
list = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    list.append([a, b, a+b])

for j in range(n):
    print("Case #%d: %d + %d = %d" % (j+1, list[j][0], list[j][1], list[j][2]))

#2438

n = int(input())
result = '*'

for i in range(1, n+1):
    print(result * i)

#2439

n = int(input())
result = '*'
blank = ' '

for i in range(1, n+1):
    print(blank * (n-i) + result * i)

#10871

n, x = map(int, input().split())
data = list(map(int, input().split()))
result = []

for i in range(n):
    if x > data[i]:
        result.append(data[i])

for j in range(len(result)):
    print(result[j], end = ' ')


