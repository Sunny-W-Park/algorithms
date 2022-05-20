#5355

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    s = list(map(str, input().split()))
    start = float(s[0])
    for i in range(1, len(s)):
        if s[i] == '@':
            start = start * 3
        if s[i] == '%':
            start = start + 5
        if s[i] == '#':
            start = start - 7
    print("%.2f" % start)
