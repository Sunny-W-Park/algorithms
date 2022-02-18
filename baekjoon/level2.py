#1330

a, b = map(int, input().split())
if a > b:
    print(">")
elif a < b:
    print("<")
elif a == b:
    print("==")

#9498

score = int(input())

if 100 >= score >= 90:
    print("A")
elif 89 >= score >= 80:
    print("B")
elif 79 >= score >= 70:
    print("C")
elif 69 >= score >= 60:
    print("D")
else:
    print("F")

#2753

year = int(input())

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("1")
else:
    print("0")

#2754

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("1")
elif x < 0 and y > 0:
    print("2")
elif x < 0 and y < 0:
    print("3")
elif x > 0 and y < 0:
    print("4")

#2844

H, M = map(int, input().split())

if M - 45 < 0:
    M = 60 - (45 - M)
    if H == 0:
        H = 23
        print(H, M)
    else:
        H = H - 1
        print(H, M)

else:
    M = M - 45
    H = H
    print(H, M)

#2525

A, B = map(int, input().split())
C = int(input())

C_time = C // 60
C_minute = C - (C_time * 60)

A = A + C_time
B = B + C_minute

if B >= 60:
    B = B - 60
    A = A + 1

while A >= 24:
    A = A - 24

print(A, B)

#2480

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

if a == b and b == c:
    print(10000 + a * 1000)

elif a == b and b != c:
    print(1000 + a * 100)

elif b == c and a != b:
    print(1000 + b * 100)

elif a == c and a != b:
    print(1000 + a * 100)

elif a != b and b != c:
    print(max(a, b, c) * 100)


