#1905

n = int(input())


#1904
import sys
sys.setrecursionlimit(1000000)

n = int(input())
k = 0

def recursive_sum(n):
    if n >= 1:
        global k
        k += n
        recursive_sum(n-1)

recursive_sum(n)
print(k)

#1903

a, b = map(int, input().split())
def recursive_odd(a, b):
    if a <= b:
        if a % 2 == 1:
            print(a)
        recursive_odd(a+1, b)

recursive_odd(a, b)

#1902

n = int(input())

def recursive_print(n):
    if n >= 1:
        print(n)
        recursive_print(n-1)

recursive_print(n)

#1901

n = int(input())
m = n

def recursive_print(n):
    if n >= 1:
        k = n - 1
        print(m - k)
        recursive_print(n-1)

recursive_print(n)
