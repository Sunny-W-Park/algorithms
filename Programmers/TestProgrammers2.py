def solution(arr):
    answer = []
    minv = arr[0]

    if len(arr) > 1:
        for i in range(0, len(arr)):
            if minv > arr[i]:
                minv = arr[i]
        arr.pop(arr.index(minv))
        answer = arr

    else: answer = [-1]

    return print(answer)


###Inputs

arr1 = [4, 3, 2, 1]
solution(arr1)

arr2 = [10]
solution(arr2)


### Wrong answer

#def solution(arr):
#    answer = []
#    elm  = min(arr)
#
#    if len(arr) > 1:
#        for i in range(0, len(arr)-1):
#            if elm == arr[i]:
#                arr.pop(i)
#                answer = arr
#
#    else: answer = [-1]
#
#    return answer
#

