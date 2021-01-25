#Selection Sort

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
            #가장 작은 인덱스를 저장
    arr[i], arr[min_index] = arr[min_index], arr[i]
    #for i in range(): 인덱스 0부터 len(arr)까지 정렬 반복

print(arr)


#Insertion Sort

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break;

print(arr)


#Quick Sort

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(arr))


