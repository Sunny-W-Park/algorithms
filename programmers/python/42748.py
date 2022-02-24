#42748

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    for c in range(len(commands)):
        narr = []
        i = commands[c][0]
        j = commands[c][1]
        k = commands[c][2]
        for p in range(i-1, j):
            narr.append(array[p])
        narr = sorted(narr)
        answer.append(narr[k-1])
    return answer

solution(array, commands)


