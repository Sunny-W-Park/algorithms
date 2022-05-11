#14425

N, M = map(int, input().split())
dict = {}
for _ in range(N):
    s = input()
    if s in dict:
        dict[s] += 1
    else:
        dict[s] = 1

result = 0
for _ in range(M):
    check = input()
    if check in dict:
        result += 1
    else:
        continue

print(result)

#1764

N, M = map(int, input().split())
dict_a = {}
for _ in range(N):
    p = input()
    if p in dict_a:
        dict_a[p] += 1
    else:
        dict_a[p] = 1
print(dict_a)

result = []
for _ in range(M):
    p = input()
    if p in dict_a:
        result.append(p)

print(len(result))
for i in sorted(result):
    print(i)

#1269

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

C = (A-B)
D = (B-A)
print(len(C) + len(D))

