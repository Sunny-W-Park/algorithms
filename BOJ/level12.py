import sys


#2750

n = int(input())
list = []

for i in range(n):
    list.append(int(input()))

list.sort()

for i in range(n):
    print(list[i])

#2751

n = int(input())
list = []

for i in range(n):
    list.append(int(input()))

for i in sorted(list):
    print(i)


#10989

n = int(input())

check_list = [0 for _ in range(10001)]

for i in range(n):
    num = int(sys.stdin.readline())
    check_list[num] = check_list[num] + 1

for i in range(10001):
    if check_list[i] != 0:
        for j in range(check_list[i]):
            print(i)        #해당 index(i)를 횟수(j) 만큼 출력

#2108

n = int(sys.stdin.readline())

list = []
many_list = []

for i in range(n):
    list.append(int(sys.stdin.readline()))

list_sorted = sorted(list)
count = [0 for _ in range(8002)]

for i in list_sorted:
    count[i+4000] += 1

many_value = max(count)

for i in range(8002):
    if count[i] == many_value:
        many_list.append(i-4000)

#산술평균
print('{:.0f}'.format(sum(list_sorted)/n))
#중앙값
print(list_sorted[round((n-1)/2)])
#최빈값
if len(many_list) == 1:
    print(many_list[0])
else:
    print(many_list[1])
#범위
print(list_sorted[n-1] - list_sorted[0])

#1427

N = str(input())
list = []

for i in range(len(N)):
    list.append(int(N[i]))

list_sorted = sorted(list, reverse = True)

result = ''

for i in range(len(list_sorted)):
    result += str(list_sorted[i])

print(result)

#11650

N = int(input())

arr = []

for i in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])

for i in sorted(arr):
    print(i[0], i[1])

#11651

N = int(input())

arr = []

for i in range(N):
    a, b = map(int, input().split())
    arr.append([b, a])

for i in sorted(arr):
    print(i[1], i[0])




