#42895

N = 5
number = 5

def solution(N, number):
    answer = []
    stack = [[]] + [[int(str(N)*i)] for i in range(1, 9)]

    for i in range(9):
        if number in stack[i]:
            return i

    for i in range(2, 9):
        for j in range(1, i):
            for a in stack[i-j]:
                for b in stack[j]:
                    stack[i].append(a+b)
                    stack[i].append(a-b)
                    stack[i].append(a*b)
                    if b!= 0:
                        stack[i].append(a//b)
        if number in stack[i]:
            return i
        stack[i] = list(set(stack[i]))

    return -1

solution(N, number)

