import sys, math

#-------BOJ--------

N = int(input())

start = 0
movies = []

def series(x):
    global movies
    count = 0
    for i in range(len(str(x))):
        if str(x)[i] == '6':
            count += 1
        if count == 3:
            movies.append(x)
            break
        elif str(x)[i] != '6':
            count = 0

while len(movies) != N:
    start += 1
    series(start)

print(movies[-1])

#1018 "재풀이(1)"

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]

count = []

for i in range(N - 7):
    for j in range(M - 7):
        count_w, count_b = 0, 0
        for p in range(i, i + 8):
            for q in range(j, j + 8):
                if (p + q) % 2 == 0:
                    if arr[p][q] != 'W':
                        count_w += 1
                    if arr[p][q] != 'B':
                        count_b += 1
                elif (p + q) % 2 == 1:
                    if arr[p][q] != 'B':
                        count_w += 1
                    if arr[p][q] != 'W':
                        count_b += 1
        count.append(count_w)
        count.append(count_b)

print(min(count))

#1018 "재풀이 요망"

input = sys.stdin.readline
N, M = map(int, input().split())
arr_str = []
arr_int = [[0 for _ in range(M)] for _ in range(N)]
arr_chess = [[0 for _ in range(8)] for _ in range(8)]
for i in range(N):
    arr_str.append(str(input().rstrip()))

for i in range(N):
    for j in range(M):
        if arr_str[i][j] == 'B':
            arr_int[i][j] = 1
        else:
            arr_int[i][j] = 0

row_limit = M - 8
col_limit = N - 8
arr_count = []
count = 0

for p in range(col_limit+1):
    for q in range(row_limit+1):
        for i in range(8):
            for j in range(8):
                arr_chess[i][j] = arr_int[i+p][j+q]
                if i == 0 and j != 0:
                    if arr_chess[i][j] == arr_chess[i][j-1]:
                        count += 1
                        if arr_chess[i][j] == 0: arr_chess[i][j] = 1
                        else: arr_chess[i][j] = 0

                if i != 0 and j == 0:
                    if arr_chess[i][j] == arr_chess[i-1][j]:
                        count += 1
                        if arr_chess[i][j] == 0: arr_chess[i][j] = 1
                        else: arr_chess[i][j] = 0

                if 1 <= i <= 7 and 1 <= j <= 7:
                    if arr_chess[i][j] == arr_chess[i][j-1] or arr_chess[i][j] == arr_chess[i-1][j]:
                        count += 1
                        if arr_chess[i][j] == 0: arr_chess[i][j] = 1
                        else: arr_chess[i][j] = 0
        arr_count.append(count)

print(arr_count)
print(min(arr_count))


#7568

input = sys.stdin.readline
N = int(input())
profile = []
rank = [1 for _ in range(N)]
for i in range(N):
    profile.append(list(map(int, input().split())))


for i in range(N):
    for j in range(N):
        if profile[i][0] < profile[j][0] and profile[i][1] < profile[j][1]:
            rank[i] = rank[i] + 1

for i in rank:
    print(i, end = ' ')

#2231

input = sys.stdin.readline
N = int(input())
result = []

a = 0

def function(a):
    num = a
    for i in range(len(str(a))):
        num += int(str(a)[i])
    return num

while a <= N:
    a += 1
    if function(a) == N:
        result.append(a)
        break

if len(result) == 0:
    print(0)
else:
    print(result[0])


#2798

input = sys.stdin.readline
a, b = map(int, input().split())
arr = list(map(int, input().split()))
result = []

for i in range(a):
    for j in range(a):
        for k in range(a):
            num = arr[i] + arr[j] + arr[k]
            if i != j and j != k and i!= k and num <= b:
                result.append(num)

print(sorted(result)[-1])


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

#10814

N = int(input())
arr = []

for i in range(N):
    a, b = map(str, input().split())
    arr.append([int(a), i, b])

for i in sorted(arr):
    print(i[0], i[2])

#1181

N = int(input())
arr1 = set()
arr2 = []

for i in range(N):
    word = str(input())
    arr1.add(word)

for i in arr1:
    arr2.append([int(len(i)), i])

for i in sorted(arr2):
    print(i[1])

#11651

N = int(input())

arr = []

for i in range(N):
    a, b = map(int, input().split())
    arr.append([b, a])

for i in sorted(arr):
    print(i[1], i[0])

#11650

N = int(input())

arr = []

for i in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])

for i in sorted(arr):
    print(i[0], i[1])


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

#2751

n = int(input())
list = []

for i in range(n):
    list.append(int(input()))

for i in sorted(list):
    print(i)

#2750

n = int(input())
list = []

for i in range(n):
    list.append(int(input()))

list.sort()

for i in range(n):
    print(list[i])

#2447

pass

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

#10870

n = int(input())

def fibo(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(n))

#10872

n = int(input())

def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1

print(factorial(n))


#1002 #재풀이 요망

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

#3053

R = int(input())

print(R ** 2 * math.pi)
print(R ** 2 * 2)

#4153

while True:
    a, b, c = map(int, input().split())
    list = []
    if a == 0 and b == 0 and c == 0:
        break
    else:
        list.append(a)
        list.append(b)
        list.append(c)
        list.sort()
        if list[0] ** 2 + list[1] ** 2 == list[2] ** 2:
            print("right")
        else:
            print("wrong")

#3009

set_x = []
set_y = []
a = 0
b = 0

for _ in range(3):
    x, y = map(int, input().split())
    set_x.append(x)
    set_y.append(y)


for i in range(3):
    if set_x.count(set_x[i]) == 1:
        a = set_x[i]
        break

for i in range(3):
    if set_y.count(set_y[i]) == 1:
        b = set_y[i]
        break

print(a, b)

#1085

x, y, w, h = map(int, input().split())
list = []

list.append(x - 0)
list.append(y - 0)
list.append(w - x)
list.append(h - y)

print(min(list))


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
        if prime[j] >= n/2:
            if n - prime[j] in prime:
                b = prime[j]
                a = n - prime[j]
                break
    print(a, b)


#4948

def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

list = list(range(2, 246912))
prime = []

for i in list:
    if isPrime(i):
        prime.append(i)

k = 1
while k != 0:
    k = int(input())
    count = 0
    if k == 0:
        break
    else:
        for i in prime:
            if k < i <= 2*k:
                count += 1
    print(count)

#1929

def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

m, n = map(int, input().split())

for j in range(m, n+1):
    if isPrime(j):
        print(j)

#11653

n = int(input())
result = n
divide = 2

while result >= divide:
    if result == 1:
        print()
        break
    else:
        if result % divide == 0:
            result = result // divide
            print(divide)
        else:
            divide = divide + 1

#2581

m = int(input())
n = int(input())
prime = []

for i in range(m, n+1):
    divisor = []
    for j in range(1, i+1):
        if i % j == 0:
            divisor.append(j)
            if len(divisor) > 2:
                pass

    if len(divisor) == 2:
        prime.append(i)

if len(prime) == 0:
    print(-1)

else:
    print(sum(prime))
    print(min(prime))


#1978

n = int(input())
numbers = input().split()

prime = []

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

for i in range(len(numbers)):
    results = []
    for j in range(1, numbers[i]+1):
        if numbers[i] % j == 0:
            results.append(numbers[i])

    if len(results) == 2:
        prime.append(numbers[i])

print(len(prime))

#1011

t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    distance = y - x
    result = 1
    n = round(distance ** (1/2))

    if distance == 1:
        result = result

    elif n ** 2 < distance:
        result += 2 * n - 1

    elif n ** 2 >= distance:
        result += 2 * n - 2

    print(result)

#2839

n = int(input())

count = 0
result = n

while True:
    if result == 0:
        print(count)
        break

    elif result > 0:
        if result % 5 == 0:
            result = result - 5
            count += 1

        elif (result - 3) % 5 == 0:
            result = result - 3
            count += 1

        elif (result - 5) % 3 == 0:
            result = result - 5
            count += 1

        elif result % 3 == 0:
            result = result - 3
            count += 1

        else:
            result = result - 3
            count += 1

    else:
        print(-1)
        break

#2775

t = int(input())
kn = [[0 for _ in range(2)] for _ in range(t)]
arr = []

for i in range(t):
    for j in range(2):
        kn[i][j] = int(input())

for i in range(t):
    arr.append([[0 for _ in range(kn[i][1])] for _ in range(kn[i][0]+1)])

for p in range(len(arr)):
    for q in range(len(arr[p][0])):
        arr[p][0][q] = q+1

count = 0

for p in range(len(arr)):
    for q in range(1, len(arr[p])):
        for r in range(len(arr[p][0])):
            count += arr[p][q-1][r]
            arr[p][q][r] = count
        count = 0

for i in range(t):
    print(arr[i][kn[i][0]][kn[i][1]-1])

#10757

a, b = map(int, input().split())
print(a+b)

#10250

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

floor = 0
room = 0
result = []

for i in range(n):
    if arr[i][2] % arr[i][0] == 0:
        floor = arr[i][0]

        if arr[i][2] // arr[i][0] >= 1:
            room = arr[i][2] // arr[i][0]

        elif arr[i][2] // arr[i][0] == 0:
            room = 1

    else:
        if arr[i][2] // arr[i][0] >= 1:
            floor = arr[i][2] % arr[i][0]
            room = arr[i][2] // arr[i][0] + 1

        elif arr[i][2] // arr[i][0] == 0:
            floor = arr[i][2] % arr[i][0]
            room = 1

    if room >= 10:
        result.append(str(floor) + str(room))

    else:
        result.append(str(floor) + '0' + str(room))

for j in range(n):
    print(int(result[j]))

#2869

import math

a, b, v = map(int, input().split())
x = (v - b) / (a - b)
x_ceil = math.ceil(x)
print(x_ceil)

#1193

x = int(input())

index_start = 1
index_end = 1
d = 1

while True:
    if index_end >= x >= index_start:
        break
    else:
        index_start = index_start + d
        d = d + 1
        index_end = index_end + d

index = x - index_start
a = 1
b = d
a = a + index
b = b - index

if d % 2 == 0:
    print(str(a) + "/" + str(b))

else:
    print(str(b) + "/" + str(a))

#2292

n = int(input())

i = 0
start = 1
end = 1

while True:
    if end >= n >= start:
        print(i+1)
        break
    else:
        i = i+1
        start = end + 1
        end = end + 6 * i

#1712

a, b, c = map(int, input().split())

q = 0

if b >= c:
    q = -1

else:
    q = a // (c-b) + 1

print(q)

#1316

n = int(input())
words = []
result = 0

for _ in range(n):
    words.append(str(input()))

words_shorten = []
for i in range(n):
    s = ''
    for j in range(len(words[i])):
        if j == 0:
            s = s + words[i][j]
        else:
            if words[i][j] != s[-1]:
                s = s + words[i][j]
    words_shorten.append(s)

for p in range(len(words_shorten)):
    checker = set()
    for q in range(len(words_shorten[p])):
        checker.add(words_shorten[p][q])
    if len(checker) == len(words_shorten[p]):
        result += 1

print(result)

#2941

s = str(input())
words = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0

for i in range(len(s)):
    if len(s)-1 > i:
        for j in range(len(words)):
            if s[i]+s[i+1] == words[j]:
                count += 1
    if len(s)-2 > i:
        for j in range(len(words)):
            if s[i]+s[i+1]+s[i+2] == words[j]:
                count += 1

print(len(s) - count)

#5622

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
results = 0

s = str(input())

for i in range(len(s)):
     for j in range(len(dial)):
         for k in range(len(dial[j])):
             if dial[j][k] == s[i]:
                 results += j+3

print(results)

#2908

a, b = map(str, input().split())
list = []
a_reverse = a[2]+a[1]+a[0]
b_reverse = b[2]+b[1]+b[0]
list.append(a_reverse)
list.append(b_reverse)

print(max(list))

#1152

words = input().split()
print(len(words))

#1157

s = str(input()).lower()

list = [0 for _ in range(123)]

for i in range(len(s)):
    for j in range(97, 123):
        if chr(j) == s[i]:
            list[j] += 1

max = 0
result = []

for k in range(123):
    if list[k] > max:
        max = list[k]

for k in range(123):
    if list[k] == max:
        result.append(chr(k))

if len(result) > 1:
    print("?")

elif len(result) == 1:
    print(result[0].upper())

#2675

t = int(input())

array = []

for _ in range(t):
    array.append(list(input().split()))

for i in range(t):
    array[i][0] = int(array[i][0])
    array[i][1] = str(array[i][1])

for i in range(t):
    result = ''
    for p in range(len(array[i][1])):
        result = result + str(array[i][1][p]) * array[i][0]
    print(result)

#10809

s = str(input())

list = [-1 for _ in range(123)]

for i in range(len(s)):
    for j in range(97, 123):
        if chr(j) == s[i]:
            if list[j] == -1:
                list[j] = i

for k in range(97, 123):
    print(list[k], end = ' ')

#11720

p = input()
q = input()
list = []

for i in range(len(str(q))):
    list.append(int(q[i]))

print(sum(list))

#11654

n = input()
print(ord(n))

#1065 

n = int(input())
list = []

for i in range(1, n+1):
    if 100 > i:
        list.append(i)

    elif 1000 > i >= 100:
        check = []
        for j in range(len(str(i))):
            check.append(int(str(i)[j]))

        if check[2] - check[1] == check[1] - check[0]:
            list.append(i)

print(len(list))

#4673

#natural_num = set(range(1, 10001))
#generated_num = set()
#
#for i in range(1, 10001):
#    for j in str(i):
#        i += int(j)
#    generated_num.add(i)
#
#result_num = sorted(natural_num - generated_num)
#
#for k in result_num:
#    print(k)

#15596

def solve(a: list) -> int:
    ans = 0
    for i in range(len(a)):
        ans += a[i]
    return ans

#4344

n = int(input())
arr = [0 for _ in range(n)]

for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().split()))

avg = [0 for _ in range(n)]

for j in range(n):
    avg[j] = (sum(arr[j]) - arr[j][0]) / arr[j][0]

count = [0 for _ in range(n)]

for p in range(n):
    for q in range(arr[p][0]+1):
        if q >= 1:
            if arr[p][q] > avg[p]:
                count[p] += 1

for x in range(n):
    count[x] = float((count[x] / arr[x][0]) * 100)
    print('{:.3f}%'.format(count[x]))


#8958

n = int(input())
list = []

for i in range(n):
    list.append(str(input()))

count = []

for j in range(n):
    count.append([0 for k in range(len(list[j]))])

for p in range(n):
    for q in range(len(list[p])):
        if list[p][q] == 'O':
            count[p][q] = 1

for p in range(n):
    for q in range(len(count[p])):
        if q >= 1:
            if count[p][q] >= 1 and count[p][q-1] >= 1:
                count[p][q] = count[p][q-1] + 1

for x in range(n):
    print(sum(count[x]))


#1546

n = int(input())

list = list(map(int, sys.stdin.readline().split()))

max = list[0]

for i in range(n):
    if list[i] > max:
        max = list[i]

result = []

for j in range(n):
    result.append(list[j] / max * 100)

print(sum(result) / n)

#3052

list = []

for i in range(10):
    list.append(int(sys.stdin.readline()) % 42)

result = [1 for _ in range(10)]

for j in range(10):
    for k in range(10):
        if j != k:
            if list[j] == list[k]:
                result[j] = 0

        elif j == k:
            if list[j] == list[k]:
                result[j] = 1

print(result)
print(sum(result))

#2577

list = []

for i in range(3):
    list.append(int(sys.stdin.readline()))

result = [str(list[0] * list[1] * list[2])]

count = [0 for x in range(10)]

for m in range(len(result[0])):
    for n in range(10):
        if result[0][m] == str(n):
            count[n] += 1

for k in range(10):
    print(count[k])

#2562

list = []

for i in range(9):
    list.append(int(sys.stdin.readline()))

max = list[0]
index = 0

for j in range(9):
    if list[j] > max:
        max = list[j]
        index = j+1
    elif list[j] == max:
        index = j+1

print(max)
print(index)


#10810

n = int(input())
ints = list(map(int, sys.stdin.readline().split()))

min = ints[0]
max = ints[0]

for i in range(n):
    if ints[i] < min:
        min = ints[i]

for j in range(n):
    if ints[j] > max:
        max = ints[j]

print(min, max)


#1110

n = int(input())

k = n
cycle = 0

while True:
    a = k // 10
    b = k % 10
    c = (a + b) % 10
    k = (b * 10) + c
    cycle += 1
    if k == n:
        break

print(cycle)

#10951

while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)
    except:
        break

#10952

a, b = 1, 1
list = []

while True:
    a, b = map(int, input().split())
    if a != 0 and b != 0:
        list.append(a+b)
    elif a == 0 and b == 0:
        break

for i in range(len(list)):
    print(list[i])

#10871

n, x = map(int, input().split())
data = list(map(int, input().split()))
result = []

for i in range(n):
    if x > data[i]:
        result.append(data[i])

for j in range(len(result)):
    print(result[j], end = ' ')

#2439

n = int(input())
result = '*'
blank = ' '

for i in range(1, n+1):
    print(blank * (n-i) + result * i)

#2438

n = int(input())
result = '*'

for i in range(1, n+1):
    print(result * i)

#11022

n = int(input())
list = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    list.append([a, b, a+b])

for j in range(n):
    print("Case #%d: %d + %d = %d" % (j+1, list[j][0], list[j][1], list[j][2]))

#11021

n = int(input())
list = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    list.append(a+b)

for j in range(n):
    print("Case #%d: %d" % (j+1, list[j]))

#2742

n = int(input())

result = n

for i in range(0, n):
    result = n - i
    print(result)

#2741

n = int(input())

for i in range(1, n+1):
    print(i)

#15552

t = int(input())
list = []

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    list.append(a+b)

for j in range(t):
    print(list[j])

#8393

n = int(input())

sum = 0

for i in range(1, n+1):
    sum += i

print(sum)

#10960

t = int(input())
list = []

for i in range(t):
    a, b = map(int, input().split())
    list.append(a + b)

for j in range(t):
    print(list[j])

#2739

n = int(input())

for i in range(1, 10):
    print("%d * %d = %d" % (n, i, n * i))

#2844

H, M = map(int, input().split())

if M - 45 < 0:
    M = 60 - (45 - M)
    if H == 0:
        H = 23
        print(H, M)
    else:
        H = H - 1
        print(H, M)

else:
    M = M - 45
    H = H
    print(H, M)

#2754

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("1")
elif x < 0 and y > 0:
    print("2")
elif x < 0 and y < 0:
    print("3")
elif x > 0 and y < 0:
    print("4")

#2753

year = int(input())

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("1")
else:
    print("0")

#9498

score = int(input())

if 100 >= score >= 90:
    print("A")
elif 89 >= score >= 80:
    print("B")
elif 79 >= score >= 70:
    print("C")
elif 69 >= score >= 60:
    print("D")
else:
    print("F")

#1330

a, b = map(int, input().split())
if a > b:
    print(">")
elif a < b:
    print("<")
elif a == b:
    print("==")

#2588

a = int(input())
b = int(input())
r1 = a * (b // 100)
r2 = a * ((b - (r1 / a * 100)) // 10)
r3 = a * ((b - (r1 / a * 100) - (r2 / a * 10)))
print(int(r3))
print(int(r2))
print(int(r1))
print(a * b)

#10430

A, B, C = map(int, input().split())
r1 = (A+B)%C
r2 = ((A%C) + (B%C))%C
r3 = (A*B)%C
r4 = ((A%C) * (B%C))%C
print(r1)
print(r2)
print(r3)
print(r4)

#10869

a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)

#1008

a, b = map(int, input().split())
print(a / b)

#10998

a, b = map(int, input().split())
print(a * b)

#1001

a, b = map(int, input().split())
print(a-b)

#1000

a, b = map(int, input().split())
print(a+b)

#10172

print("\
|\_/|\n\
|q p|   /}\n\
( 0 )\"\"\"\\\n\
|\"^\"`    |\n\
||_/=\\\\__|\n\
")

#10171

print("\
\    /\\\n\
 )  ( ')\n\
(  /  )\n\
 \(__)|\
 ")

#10718

for i in range(2):
    print("강한친구 대한육군")

#2557

print("Hello World!")

#-------Code Up-------

#6098

array = []

for _ in range(10):
    array.append(list(map(int, input().split())))

x, y = 1, 1

while True:
    if array[x][y] == 0:
        array[x][y] = 9
    elif array[x][y] == 2:
        array[x][y] = 9
        break

    #우측 이동
    if array[x][y+1] != 1:
        y += 1
    #하단 이동
    elif array[x+1][y] != 1:
        x += 1

    #이동 불가
    if array[x][y+1] == 1 and array[x+1][y] == 1:
        array[x][y] = 9
        break

for i in range(10):
    for j in range(10):
        print(array[i][j], end = ' ')
    print()

#6097

#입력값 저장
h, w = map(int, input().split())
n = int(input())
list = [[0 for _ in range(w)] for _ in range(h)]
stick = []
for _ in range(n):
    stick.append(input().split())

for i in range(n):
    for j in range(4):
        stick[i][j] = int(stick[i][j])

#격자판 값 변형
for p in range(n):
    for q in range(stick[p][0]):
        if stick[p][1] == 0:
            list[int(stick[p][2])-1][int(stick[p][3])-1+q] = 1
        elif stick[p][1] == 1:
            list[int(stick[p][2])-1+q][int(stick[p][3])-1] = 1

#출력
for i in range(h):
    for j in range(w):
        print(list[i][j], end = ' ')
    print()

#6096

#바둑판 저장
list = []

for _ in range(19):
    list.append(input().split())

for i in range(19):
    for j in range(19):
        list[i][j] = int(list[i][j])

#뒤집기 횟수 저장
n = int(input())

#좌표 저장
position = []

for _ in range(n):
    position.append(input().split())

for k in range(n):
    position[k][0] = int(position[k][0])
    position[k][1] = int(position[k][1])

for p in range(n):
    for q in range(19):
        if list[position[p][0]-1][q] == 0:
            list[position[p][0]-1][q] = 1

        elif list[position[p][0]-1][q] == 1:
            list[position[p][0]-1][q] = 0

        if list[q][position[p][1]-1] == 0:
            list[q][position[p][1]-1] = 1

        elif list[q][position[p][1]-1] == 1:
            list[q][position[p][1]-1] = 0

for x in range(19):
    for y in range(19):
        print(list[x][y], end = ' ')
    print(' ')

#6095

n = int(input())
position = []

for i in range(n):
    a = input().split()
    a = position.append(a)

for i in range(n):
    position[i][0] = int(position[i][0])
    position[i][1] = int(position[i][1])

list = [[0 for _ in range(19)] for _ in range(19)]

for j in range(n):
       list[position[j][0]-1][position[j][1]-1] = 1

for r in range(19):
    for q in range(19):
        print(list[r][q], end = ' ')
    print(" ")

#6094

n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

min = a[0]

for i in range(n):
    if min > a[i]:
         min = a[i]

print(min)

#6093

n = int(input())
a = input().split()

list = []

for i in range(n):
    list.append(a[-i-1])

for j in range(n):
    print(list[j], end = ' ')

#6092

n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

list = [0 for _ in range(23)]

for j in range(n):
    list[a[j]-1] += 1

for k in range(23):
    print(list[k], end = ' ')

#6091

a, b, c = map(int, input().split())

d = 1

while d % a != 0 or d % b != 0 or d % c != 0:
    d = d + 1

print(d)

#6090

a, m, d, n = map(int, input().split())
result = a
for i in range(1, n):
    result = result * m + d
print(result)

#6089

a, r, n = map(int, input().split())
result = a
for i in range(1, n):
    result = result * r
print(result)

#6088

a, r, n = map(int, input().split())
result = a
for i in range(1, n):
    result = result * r
print(result)

#6087

a, d, n = map(int, input().split())
result = a
for i in range(1, n):
    result = result + d
print(result)

#6086

n = int(input())
sum = 0
for i in range(n+1):
    if n > sum:
        sum += i
    else:
        break

print(sum)

#6085

w, h, b = map(int, input().split(" "))
MB = (w * h * b) / 8 / 2**10 / 2**10
print("{:.2f}".format(MB) + " " + "MB")

#6084

h, b, c, s = map(int, input().split(" "))
MB = (h * b * c * s) / 8 / 2**10 / 2**10
print("{:.1f}".format(MB) + " " + "MB")

#6083

r, g, b = map(int, input().split(" "))

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)

print(r * g * b)

#6082(재풀이)

n = int(input())

list = []

for i in range(1, n+1):
    if i%10 == 3 or i%10 == 6 or i%10 == 9:
        list.append("X")
    else:
        list.append(i)

for j in range(n):
    print(list[j], end = ' ')

#6082

n = int(input())

for i in range(1,n+1):

    if i%10 == 3 or i%10 == 6 or i%10 == 9: print("X", end=" ")

    else: print(i, end=" ")

#6081

n = int(input(), 16)

for i in range(1, 16):
    print("%X*%X=%X" %(n, i, (n*i)))

#6080

n, m = map(int, input().split(" "))

for i in range(1, n+1):
    for j in range(1, m+1):
        print(i, j)

#6079

a = input()
a = int(a)
b = 0
c = 0

for i in range(a):
    if a == b:
        break
    elif a > b:
        c += 1
        b = b+c
    else:
        pass

print(c)

#6078

list = [0]

while list[-1] != 'q':
    b = input()
    list.append(b)

for i in range(1, len(list)+1):
    print(list[i], end = '\n')

#6077

a = input()
a = int(a)
sum = 0

for i in range(a):
    if a != 0:
        if a % 2 == 0:
            sum += a
            a = a-1
        else:
            a = a-1

print(sum)

#6076

a = input()
a = int(a)
b = int(a)
list = []
list.append(a)

while a != 0:
    a = a-1
    list.append(a)

for i in range(1, b+2):
    print(list[-i])

#6075

a = input()
a = int(a)
b = int(a)
list = []
list.append(a)

while a != 0:
    a = a-1
    list.append(a)

for i in range(1, b+2):
    print(list[-i])

#6074

a = input()
list = []
list.append(a)
b = 97

while list[-1] != 'a':
    b = int(ord(list[-1]))-1
    list.append(chr(b))

c = ord(a) - b
#print(c)

for i in range(1, c+2):
    print(list[-i], end = ' ')


#6073

a = input()
a = int(a)

while a != 0:
    a = a-1
    print(a)

#6072

a = input()
a = int(a)

while a != 0:
    print(a)
    a = a-1

#6071

list = [1]

while list[-1] != 0:
    a = input()
    list.append(int(a))

for i in range(1, len(list)-1):
    print(list[i])

#6070

a = input()
a = int(a)
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
fall = [9, 10, 11]
if a in winter:
    print("winter")
elif a in spring:
    print("spring")
elif a in summer:
    print("summer")
elif a in fall:
    print("fall")

#6069

a = input()
a = str(a)
if a == "A":
    print("best!!!")
elif a == "B":
    print("good!!")
elif a == "C":
    print("run!")
elif a == "D":
    print("slowly~")
else:
    print("what?")

#6068

a = input()
a = int(a)
if 100 >= a >= 90:
    print("A")
elif 89 >= a >= 70:
    print("B")
elif 69 >= a >= 40:
    print("C")
elif 39 >= a >= 0:
    print("D")

#6067

a = input()
a = int(a)
if 0 >= a and a % 2 == 0:
    print("A")
elif 0 >= a and a % 2 == 1:
    print("B")
elif a >= 0 and a % 2 == 0:
    print("C")
elif a >= 0 and a % 2 == 1:
    print("D")

#6066

a, b, c = map(int, input().split(" "))

list = [a, b, c]

for i in range(3):
    if list[i] % 2 == 0:
        print("even")
    else:
        print("odd")

#6065

a, b, c = map(int, input().split(" "))
if a % 2 == 0:
    print(a)

if b % 2 == 0:
    print(b)

if c % 2 == 0:
    print(c)

#6064

a, b, c = map(int, input().split(" "))
print(min(a, b, c))

#6063

a, b = map(int, input().split(" "))
print(max(a, b))

#6062

a, b = map(int, input().split(" "))
c = a ^ b
print(c)

#6061

a, b = map(int, input().split(" "))
c = a | b
print(c)

#6060

a, b = map(int, input().split(" "))
c = a & b
print(c)

#6059

a = input()
a = int(a)
b = ~a
print(b)

#6058

a, b = map(int, input().split(" "))
if bool(a) == False and bool(b) == False:
    print("True")
else:
    print("False")

#6057

a, b = map(int, input().split(" "))
if bool(a) == bool(b):
    print("True")
else:
    print("False")

#6056

a, b = map(int, input().split(" "))
if bool(a) != bool(b):
    print("True")
else:
    print("False")

#6055

a, b = map(int, input().split(" "))
if bool(a) == True or bool(b) == True:
    print("True")
else:
    print("False")

#6054

a, b = map(int, input().split(" "))
if bool(a) == True and bool(b) == True:
    print("True")
else:
    print("False")

#6053

a = input()
a = int(a)
if bool(a) == False:
    print("True")
else:
    print("False")

#6052

a = input()
a = int(a)
if a == 0:
    print("False")
else:
    print("True")

#6051

a, b = map(int, input().split(" "))
if a != b:
    print("True")
else:
    print("False")

#6050

a, b = map(int, input().split(" "))
if b >= a:
    print("True")
else:
    print("False")

#6049

a, b = map(int, input().split(" "))
if a == b:
    print("True")
else:
    print("False")

#6048

a, b = map(int, input().split(" "))
if a < b:
    print("True")
else:
    print("False")

#6047

a, b = map(int, input().split(" "))
c = 2**b
print(a*c)

#6046

a = input()
a = int(a)
print(2*a)

#6045

a, b, c = map(int, input().split(" "))
d = a+b+c
e = (a+b+c)/3
print(d, "{:.2f}".format(e))

#6044

a, b = map(int, input().split(" "))
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print("{:.2f}".format(a/b))

#6043

a, b = map(float, input().split(" "))
print("{:.3f}".format(a/b))

#6042

a = input()
a = print(round(float(a), 2))

#6041

a, b = map(int, input().split(" "))
print(a%b)

#6040

a, b = map(int, input().split(" "))
print(a//b)

#6039

a, b = map(float, input().split(" "))
print(a**b)

#6038

a, b = map(int, input().split(" "))
print(a**b)

#6037

n = input()
n = int(n)
a = input()
a = str(a)
print(a*n)

#6036

a, n = input().split(" ")
n = int(n)
print(a*n)

#6035

a, b = map(float, input().split(" "))
print(a*b)

#6034

a, b = map(int, input().split(" "))
print(a-b)

#6033

a = input()
a = ord(a)
a = a+1
print(chr(a))

#6032

a = input()
a = int(a)
print(-a)

#6031

a = input()
a = int(a)
print(chr(a))

#6030

a = ord(input())
print(a)

#6029

a = input()
a = int(a, 16)
print('%o'% a)

#6028

a = input()
a = int(a)
print('%X'% a)

#6027

a = input()
a = int(a)
print('%x'% a)

#6026

a = input()
a = float(a)
b = input()
b = float(b)
print(a+b)

#6025

a, b = map(int, input().split(" "))
print(a+b)

#6024

a, b = map(str, input().split(" "))
print(a+b)


#6023

a = input()
if a[1] == ":":
    if a[3] == ":":
        print(a[4])
    else:
        print(a[2:4])
elif a[2] == ":":
    if a[4] == ":":
        print(a[5])
    else:
        print(a[3:5])

#6022

a = input()
print(a[0]+""+a[1]+" "+a[2]+""+a[3]+" "+a[4]+""+a[5])

#슬라이싱 사용 시

a = input()
print(a[0:2]+" "+a[2:4]+" "+a[4:6])

#6021

a = input()
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

#6020

a, b = map(str, input().split("-"))
print(a, b, sep = "")

#6019

a, b, c = map(int, input().split("."))
print(c, b, a, sep = "-")

#6018

a, b = map(int, input().split(":"))
print(a, b, sep = ":")

#6017

a = input()
print(a, a, a)

#6016

a, b = map(str, input().split(" "))
print(b + " " + a)

#6015

a, b = map(int, input().split(" "))
print(a)
print(b)

#6014

a = input()
print(float(a))
print(float(a))
print(float(a))

#6013

a = input()
b = input()
print(str(b))
print(str(a))

#6012

a = input()
b = input()
print(a)
print(b)

#6011

a = input()
print(float(a))
