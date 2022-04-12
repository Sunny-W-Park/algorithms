#1978

n = int(input())
numbers = input().split()

prime = []

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

for i in range(len(numbers)):
    results = []
    for j in range(1, numbers[i]+1):
        if numbers[i] % j == 0:
            results.append(numbers[i])

    if len(results) == 2:
        prime.append(numbers[i])

print(len(prime))

#2581

m = int(input())
n = int(input())
prime = []

for i in range(m, n+1):
    divisor = []
    for j in range(1, i+1):
        if i % j == 0:
            divisor.append(j)
            if len(divisor) > 2:
                pass

    if len(divisor) == 2:
        prime.append(i)

if len(prime) == 0:
    print(-1)

else:
    print(sum(prime))
    print(min(prime))

#11653

n = int(input())
result = n
divide = 2

while result >= divide:
    if result == 1:
        print()
        break
    else:
        if result % divide == 0:
            result = result // divide
            print(divide)
        else:
            divide = divide + 1

#1929

def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

m, n = map(int, input().split())

for j in range(m, n+1):
    if isPrime(j):
        print(j)

#4948

def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

list = list(range(2, 246912))
prime = []

for i in list:
    if isPrime(i):
        prime.append(i)

k = 1
while k != 0:
    k = int(input())
    count = 0
    if k == 0:
        break
    else:
        for i in prime:
            if k < i <= 2*k:
                count += 1
    print(count)


#9020

def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

numbers = list(range(2, 10001))
prime = []
for i in numbers:
    if isPrime(i):
        prime.append(i)

t = int(input())

for i in range(t):
    n = int(input())
    a = 0
    b = 0
    for j in range(len(prime)):
        if prime[j] >= n/2:
            if n - prime[j] in prime:
                b = prime[j]
                a = n - prime[j]
                break
    print(a, b)

#1085

x, y, w, h = map(int, input().split())
list = []

list.append(x - 0)
list.append(y - 0)
list.append(w - x)
list.append(h - y)

print(min(list))

#3009

set_x = []
set_y = []
a = 0
b = 0

for _ in range(3):
    x, y = map(int, input().split())
    set_x.append(x)
    set_y.append(y)


for i in range(3):
    if set_x.count(set_x[i]) == 1:
        a = set_x[i]
        break

for i in range(3):
    if set_y.count(set_y[i]) == 1:
        b = set_y[i]
        break

print(a, b)

#4153

while True:
    a, b, c = map(int, input().split())
    list = []
    if a == 0 and b == 0 and c == 0:
        break
    else:
        list.append(a)
        list.append(b)
        list.append(c)
        list.sort()
        if list[0] ** 2 + list[1] ** 2 == list[2] ** 2:
            print("right")
        else:
            print("wrong")

#3053

R = int(input())

print(R ** 2 * math.pi)
print(R ** 2 * 2)

#1002

t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(float, input().split())
    d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

    if d == 0 and r1 == r2:
        print(-1)

    elif r1 + r2 == d or abs(r1 - r2) == d:
        print(1)

    elif abs(r1 - r2) < d < r1 + r2:
        print(2)

    else:
        print(0)


