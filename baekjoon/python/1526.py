
#1066

N = int(input())

while N != 0:
    result = 0
    for i in range(len(str(N))):
        if str(N)[i] == '4' or str(N)[i] == '7':
            result += 1
        else:
            continue
    if result == len(str(N)):
        print(N)
        break
    N -= 1


