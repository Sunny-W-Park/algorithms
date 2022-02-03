#Top-down

d = [0] * 100

def fibo(n):
    if n == 1 or n == 2:
        return 1
    if d[n] != 0:
        return d[n]
    d[n] = fibo(n) + fibo(n-1)
    return d[n]

#Bottom-up

n = int(input())

d = [0] * 100

d[1] = 1
d[2] = 1

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])

