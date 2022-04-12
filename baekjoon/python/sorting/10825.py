#10825

import sys
input = sys.stdin.readline
N = int(input())
grades = []
for _ in range(N):
    a, b, c, d = map(str, input().split())
    b = int(b)
    c = int(c)
    d = int(d)
    grades.append([a, b, c, d])
    
grades.sort(key=lambda x: x[0])
grades.sort(key=lambda x: x[3], reverse = True)
grades.sort(key=lambda x: x[2])
grades.sort(key=lambda x: x[1], reverse = True)

for i in grades:
    print(i[0])


