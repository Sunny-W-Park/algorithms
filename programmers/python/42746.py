#42746

numbers = [3, 30, 34, 5, 9]

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x:x*3, reverse = True)
    print(numbers)
    return str(int(''.join(numbers)))

solution(numbers)

#numbers = [6, 10, 2]
numbers = [3, 30, 34, 5, 9]

#####

def solution(numbers):
    l = len(str(max(numbers)))
    
    n_numbers = []
    for i in numbers:
        k = l - len(str(i))
        n_numbers.append([i*10**k, k])
    
    answer = ''
    for i in sorted(n_numbers, reverse = True):
        if i[1] > 0:
            answer += str(i[0] // 10**i[1])
        if i[1] == 0:
            answer += str(i[0])
    return answer

#####

def solution(numbers):
    l = 0
    for i in range(len(numbers)):
        l += int(len(str(numbers[i])))

    n_numbers = []
    for i in numbers:
        k = l - len(str(i))
        n_numbers.append(i * 10**k)

    print(sorted(n_numbers, reverse = True))

    result = 0
    for i in range(len(n_numbers)):
        result += sorted(n_numbers, reverse = True)[i] // 10**i

    answer = str(result)

    return answer

