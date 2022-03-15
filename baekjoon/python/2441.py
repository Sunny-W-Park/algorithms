#2441

import sys
input = sys.stdin.readline
N = int(input())
blank = 0
while N!=0:
    print(' ' * blank + '*' * N)
    N -= 1
    blank += 1

