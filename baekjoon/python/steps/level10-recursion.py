#10872

n = int(input())

def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1

print(factorial(n))

#10870

n = int(input())

def fibo(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(n))

#2447

pass

#11729

n = int(input())
list = []

def hanoi(n, x, y):
    global list
    if n > 1:
        hanoi(n - 1, x, 6 - x - y)

    list.append([x, y])

    if n > 1:
        hanoi(n - 1, 6 - x - y, y)

hanoi(n, 1, 3)
print(len(list))
for i in range(len(list)):
    print(list[i][0], list[i][1])


