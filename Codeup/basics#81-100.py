#basics #81-100

#97

arr = [0 for i in range(19)]
for i in range(19):
    arr[i] = list(map(int, input().split()))

num = int(input())
for t in range(num):
    x, y = map(int, input().split())
    for l in range(19):
        if arr[x-1][l] == 0:
            arr[x-1][l] = 1
        else:
            arr[x-1][l] = 0
    for l in range(19):
        if arr[l][y-1] == 0:
            arr[l][y-1] = 1
        else:
            arr[l][y-1] = 0

for m  in range(19):
    for n in range(19):
        print(arr[m][n],  end = ' ')
    print()

#96

n = int(input())
arr = [[0 for i in range(19)] for j in range(19)]
for k in range(n):
    i, j = map(int, input().split())
    arr[i-1][j-1] = 1
for i in range(19):
    for j in range(19):
        print(arr[i][j], end = ' ')
    print()

#95

n = int(input())
arr = list(map(int, input().split()))

def findmin(n, arr):
    minv = arr[0]
    for i in range(n):
        if arr[i] < minv:
            minv = arr[i]
    print(minv)

findmin(n, arr)

#94

n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
for i in range(n):
    print(arr[i], end = ' ')

#93

n = int(input())
arr = list(map(int, input().split(" ")))

def studentcall(n, arr):
    stu = list(0 for i in range(23))
    for i in range(n):
        stu[arr[i]-1] = stu[arr[i]-1] + 1
        #arr 배열값을 index 삼아 또 다른 배열을 만들어준다.
    for j in range(23):
        print(stu[j], end = ' ')

studentcall(n, arr)

#1024

a = input()
a = str(a)

def breakword(word):
    answer = ''
    for i in range(0, len(word)):
        answer = word[i]
        print('\'' + answer + '\'')

breakword(a)

#84

r, g, b = map(int, input().split(" "))

def rgb(r, g, b):
    x = 0
    y = 0
    z = 0
    for i in range(0, r):
        x = i
        for l in range(0, g):
            y = l
            for k in range(0, b):
                z = k
                print(x, y, z)
    print(r * g * b)

rgb(r, g, b)

#81

n, m = map(int, input().split(" "))

def combination(n, m):
    a = 0
    b = 0
    for i in range(1, n+1):
        a = i
        for l in range(1, m+1):
            b = l
            print(a, b)

combination(n, m)

#92

a, b, c = map(int, input().split(" "))

def leastcom(a, b, c):
    day = 0
    while day >= 0:
        day = day + 1
        if day % a == 0 and day % b == 0 and day % c == 0:
            break;
    print(day)

leastcom(a, b, c)

#91

a, m, d, n = map(int, input().split(" "))

def customseq(a, m, d, n):
    answer = a
    for i in range(1, n+1):
        if i == 1:
            answer = answer
        elif i > 1:
            answer = answer*m + d
    print(answer)

customseq(a, m, d, n)

#90

a, r, n = map(int, input().split(" "))

def geosequence(a, r, n):
    seq = n-1
    print(a * r**seq)

geosequence(a, r, n)

#89

a, d, n = map(int, input().split(" "))

def sequence(a, d, n):
    seq = n-1
    print(a + d*seq)

sequence(a, d, n)

#88

a = input()
a = int(a)

def passthree(k):
    answer = ''
    for i in range(1, k+1):
        if i%3 == 0:
            answer = answer + ""
        elif i == 1:
            answer = answer + str(i)
        else:
            answer = answer + " " + str(i)

    print(answer)

passthree(a)

#84

a = input()
a = int(a)

def smallsum(k):
    sumv = 0
    for i in range(1, k+1):
        if k > sumv:
            sumv = sumv + i
        else: break;

    print(sumv)

smallsum(a)

#83

a = input()
a = int(a)

def threesixnine(k):
    answer = ''
    for i in range(1, k+1):
        if i % 3 == 0:
            answer = answer + " X"
        elif i == 1:
            answer = answer + str(i)
        else:
            answer = answer + " "+ str(i)

    print(answer)

threesixnine(a)
