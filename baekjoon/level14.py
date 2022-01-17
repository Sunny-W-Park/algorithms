#15649

sys.setrecursionlimit(10000)

input = sys.stdin.readline
N, M = map(int, input().split())
s = []

def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(1, N + 1):
        if i in s:
            continue
        s.append(i)
        dfs()
        s.pop()

dfs()

#15650

sys.setrecursionlimit(10000)

input = sys.stdin.readline
N, M = map(int, input().split())
s = []

def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(1, N + 1):
        if i in s:
            continue
        if len(s) > 0:
            if i < s[-1]:
                continue
        s.append(i)
        dfs()
        s.pop()

dfs()

#15651

sys.setrecursionlimit(10000)

input = sys.stdin.readline
N, M = map(int, input().split())
s = []

def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(1, N + 1):
        s.append(i)
        dfs()
        s.pop()

dfs()

#15652

sys.setrecursionlimit(10000)

input = sys.stdin.readline
N, M = map(int, input().split())
s = []

def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(1, N + 1):
        if len(s) > 0:
            if i < s[-1]:
                continue
        s.append(i)
        dfs()
        s.pop()

dfs()


