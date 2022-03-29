#18258

from collections import deque
q = deque()
N = int(input())
for _ in range(N):
    order = list(input().split())
    if order[0] == 'push':
        q.append(int(order[1]))
    if order[0] == 'front':
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)
    if order[0] == 'back':
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)
    if order[0] == 'size':
        if len(q) > 0:
            print(len(q))
        else:
            print(0)
    if order[0] == 'empty':
        if len(q) > 0:
            print(0)
        else:
            print(1)
    if order[0] == 'pop':
        if len(q) > 0:
            print(q[0])
            del q[0]
        else:
            print(-1)
    print(q)


