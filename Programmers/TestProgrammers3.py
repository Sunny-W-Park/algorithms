#직사각형 출력하기

a, b = map(int, input().strip().split(' '))
for x in range(b):
    for y in range(a):
        print('*', end = '')
    print()


def solution(a, b):
    answer = 0
    if b >= a:
     	for i in range(a, b+1):
            answer = answer + i
    else:
        for i in range(a, b-1, -1):
            answer = answer + i
    print(answer)

solution(5, 3)
