#2022.01.07

#18870

#dict 개념 참고

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr_set_sorted = sorted(set(arr))

dic = {arr_set_sorted[i] : i for i in range(len(arr_set_sorted))}

for i in range(len(arr)):
    print(dic[arr[i]], end = ' ')

#내 풀이

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr_set = set()

for i in range(N):
    arr_set.add(arr[i])

for i in range(N):
    for j in range(len(arr_set)):
        if arr[i] == sorted(arr_set)[j]:
            arr[i] = j
    print(arr[i], end = ' ')


#2022.01.05

#10989

n = int(input())

check_list = [0 for _ in range(10000)]

for i in range(n):
    num = int(input())
    check_list[num - 1] = check_list[num - 1] + 1

for i in range(len(check_list)):
    if check_list[i] != 0:
        for j in range(check_list[i]):
            print(i + 1)        #해당 index(i+1)를 횟수(j) 만큼 출력


#2021.12.16

#11729

n = int(input())
list = []

def hanoi(n, x, y):
    global list
    if n > 1:
        hanoi(n - 1, x, 6 - x - y)

    list.append([x, y])

    if n > 1:
        hanoi(n - 1, 6 - x - y, y)

hanoi(n, 1, 3)
print(len(list))
for i in range(len(list)):
    print(list[i][0], list[i][1])

#1002

t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(float, input().split())
    d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

    if d == 0 and r1 == r2:
        print(-1)

    elif r1 + r2 == d or abs(r1 - r2) == d:
        print(1)

    elif abs(r1 - r2) < d < r1 + r2:
        print(2)

    else:
        print(0)


#4673

natural_num = set(range(1, 10001))
generated_num = set()
#set 자료형의 특징
#1) 순서 없음 -> sort로 정렬 필요
#2) 중복 없음 -> 데이터 입력시 중복을 차단해주는 역할 수행

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generated_num.add(i)

result_num = sorted(natural_num - generated_num)

for k in result_num:
    print(k)


#2021.12.28 

#9020

def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

numbers = list(range(2, 10001))
prime = []
for i in numbers:
    if isPrime(i):
        prime.append(i)

t = int(input())

for i in range(t):
    n = int(input())
    a = 0
    b = 0
    for j in range(len(prime)):
        if prime[j] >= n/2:         ##2로 나눈 중간값부터 탐색
            if n - prime[j] in prime:       ## "in prime" 으로 다른 수 탐색
                b = prime[j]
                a = n - prime[j]
                break       ##break를 통해 j가 range의 끝까지 탐색하는 것을 방지
    print(a, b)

