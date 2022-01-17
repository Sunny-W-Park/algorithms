#Binary Search

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    #중간점 인덱스: 실수일 경우 소수부분 ignore

    if array[mid] == target:
        return mid
    #[mid] == target

    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    #왼쪽탐색, 끝이 mid -1 로 한단위 줄어듬

    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
    #오른쪽탐색, 시작이 mid + 1 로 한단위 올라감

n, target = map(int, (input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
    print("there is no target")

else:
    print("%d 번째 칸에 있습니다." % (result + 1))
