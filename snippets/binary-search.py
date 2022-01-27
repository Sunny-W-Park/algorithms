#Binary Search

#recursive

def binary_search(data, start, target, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if data[mid] == target:
        return mid
    if data[mid] < target:
        binary_search(data, mid+1, target, end)
    if data[mid] > target:
        binary_search(data, start, target, mid-1)

#iteration

def binary_search(data, start, target, end):
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            end = mid - 1
        elif data[mid] < target:
            start = mid + 1
        else:
            return None


