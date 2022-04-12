#9012

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    case = input()
    stack = []
    stack.append(case[0])
    for i in range(1, len(case)):
        if case[i] == '(':
            stack.append(case[i])
        elif case[i] == ')':
            if len(stack) > 0 and stack[-1] == '(':
                del stack[-1]
            else:
                stack.append(case[i])
    if len(stack) > 0:
        print("NO")
    else:
        print("YES")


#10828

import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    case = list(map(str, input().split()))
    if case[0] == 'push':
        stack.append(int(case[1]))
    if case[0] == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
    if case[0] == 'size':
        print(len(stack))
    if case[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if case[0] == 'pop':
        if len(stack) > 0:
            x = stack.pop()
            print(x)
        else:
            print(-1)



