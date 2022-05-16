#14650

import sys

sys.setrecursionlimit(100000)

N = int(input())
res = 0

def make_num(n, s):
    global res
    for i in range(3):
        if n == 0 and i == 0:
            continue
        if n == N:
            if s % 3 == 0:
                res += 1
                return res
        else:
            make_num(n+1, int(str(s+i)))

make_num(0, 0)
print(res)

