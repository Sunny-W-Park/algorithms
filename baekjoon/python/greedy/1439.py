#1439

import sys
input = sys.stdin.readline
S = input()

result = int(10**9)

cnt = 0
flag = False
for i in range(len(S)):
    if S[i] == '0' and flag == False:
        flag = True
        cnt += 1
    if S[i] == '1':
        flag = False
result = min(result, cnt)

cnt = 0
flag = False
for i in range(len(S)):
    if S[i] == '1' and flag == False:
        flag = True
        cnt += 1
    if S[i] == '0':
        flag = False
result = min(result, cnt)

print(result)
