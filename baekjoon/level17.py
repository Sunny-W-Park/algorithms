#2004 재풀이

input = sys.stdin.readline
n, m = map(int, input().split())

def count(n, k):
    count = 0
    while n > 1:
        n = n // k
        count += n
    return count

count_five = count(n, 5) - (count(n - m, 5) + count(m, 5))
count_two = count(n, 2) - (count(n - m, 2) + count(m, 2))
print(min(count_two, count_five))

#1676

sys.setrecursionlimit(10**4)

input = sys.stdin.readline
N = int(input())

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(N)
count = 0
for i in range(len(str(result))-1, -1, -1):
    if str(result)[i] != '0':
        print(count)
        break
    elif str(result)[i] == '0':
        count += 1

#5086

a, b = 1, 1
while a!= 0 and b!= 0:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')

#1037

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)

if len(arr) == 1:
    print(arr[0] * arr[0])

else:
    print(arr[0] * arr[-1])

#1934 재풀이

input = sys.stdin.readline
N = int(input())

def lcd(A, B):
    if B == 0:
        return A
    else:
        return lcd(B, A % B)

def gcm(A, B):
    return (A * B) // lcd(A, B)

for _ in range(N):
    A, B = map(int, input().split())
    print(gcm(A, B))

#3036

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))

div = arr[0]

def lcd(A, B):
    if B == 0:
        return A
    else:
        return lcd(B, A % B)

for i in range(1, N):
    A = div // lcd(div, arr[i])
    B = arr[i] // lcd(div, arr[i])
    print(str(A) + "/" + str(B))


#11050

input = sys.stdin.readline
N, K = map(int, input().split())

def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1

def binominal_coefficient(n, k):
    return factorial(n) // (factorial(n - k) * factorial(k))

print(binominal_coefficient(N, K))

#1010

input = sys.stdin.readline
T = int(input())

def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1

def binominal_coefficient(n, k):
    return factorial(n) // (factorial(n - k) * factorial(k))

for _ in range(T):
    N, M = map(int, input().split())
    print(binominal_coefficient(M, N))


