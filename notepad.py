import sys

#-------BOJ-------

#1065 **재풀이 요망**

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
