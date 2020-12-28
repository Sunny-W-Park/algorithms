### 재풀이 요망


def solution(arr):
    answer = []
    elm  = min(arr)

    if len(arr) > 1:
        for i in range(0, len(arr)-1):
            if elm == arr[i]:
                arr.pop(i)
                answer = arr

    else: answer = [-1]

    return answer


### Inputs

arr1 = [4, 3, 2, 1]
solution(arr1)

arr2 = [10]
solution(arr2)


def plusfour(k):
    print(k+4)

m = 1
plusfour(m)
