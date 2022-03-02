#두 배열의 원소 교체

N, K = map(int, input().split())
arrA = sorted(list(map(int, input().split())))
arrB = sorted(list(map(int, input().split())))

for i in range(K):
    if arrA[i] < arrB[-i-1]:
        arrA[i] = arrB[-i-1]

print(sum(arrA))


#성적이 낮은 순서로 학생 출력

n = int(input())
arr = []
newarr = []
for i in range(n):
    arr.append(list(map(str, input().split(" "))))

for i in range(n):
    newarr.append(tuple([ int(arr[i][1]), arr[i][0] ]))

newarr_sorted = sorted(newarr)

for i in range(n):
    print(newarr_sorted[i][1], end = ' ')


#위에서 아래로

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

arr = sorted(arr, reverse = True)

for i in range(n):
    print(arr[i], end = ' ')


