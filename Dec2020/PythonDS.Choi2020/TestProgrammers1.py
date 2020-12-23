def solution(num):
    answer = 0
    while num > 1:
        if num % 2 == 0:
            num = num/2
            answer += 1

        else:
            num = num*3 + 1
            answer += 1

    if answer < 500:
        print(answer)

    else:
        print(-1)

solution(6)
solution(16)
solution(626331)
