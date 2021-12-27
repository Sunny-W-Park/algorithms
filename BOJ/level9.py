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


