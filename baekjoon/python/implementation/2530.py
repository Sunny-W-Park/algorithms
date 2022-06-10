#2530

A, B, C = map(int, input().split())
D = int(input())
while D > 0:
    D -= 1
    if C < 60:
        C += 1
        if C == 60:
            B += 1
            C = 0
            if B >= 60:
                A += 1
                B = 0
                if A == 24:
                    A = 0

print(A, B, C)

