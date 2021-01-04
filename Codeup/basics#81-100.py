#basics #81-100

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
