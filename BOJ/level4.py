#10952

a, b = 1, 1
list = []

while True:
    a, b = map(int, input().split())
    if a != 0 and b != 0:
        list.append(a+b)
    elif a == 0 and b == 0:
        break

for i in range(len(list)):
    print(list[i])

#10951

while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)
    except:
        break

#1110

n = int(input())

k = n
cycle = 0

while True:
    a = k // 10
    b = k % 10
    c = (a + b) % 10
    k = (b * 10) + c
    cycle += 1
    if k == n:
        break

print(cycle)

