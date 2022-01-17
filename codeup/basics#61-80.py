### basics #61-80

###후기

#79

arr = list(map(str, input().split()))
index = 0
for i in range(0, len(arr)):
    if arr[i] == 'q':
        index = i
        break;
        #n번째 q는 찾지 않는다.
for j in range(0, index+1):
    print(arr[j])

#76

let = input(str())
arr = []
for i in range(ord("a"), ord(let)+1):
    arr.append(chr(i))
for j in range(0, len(arr)):
    print(arr[j], end = " ")

###전기

#80

a = input()
a = int(a)

def sumtil(k):
    sum = 0
    for n in range(0, k):
            sum = sum + n
            if sum >= k:
                break;
    print(n)

sumtil(a)


#78

a = input()
a = int(a)

def sumeven(k):
    sum = 0
    for i in range(0, k+1):
        if i % 2 == 0:
            sum = sum+i
    print(sum)

sumeven(a)

#77

a = input()
a = int(a)

def countup(item):
    printout = -1
    while printout < item:
        printout = printout + 1
        print(printout)

countup(a)

#75

a = input()
a = int(a)

def countdown(item):
    count = item
    for n in range(1, item+1):
        count = item - n
        print(count)

countdown(a)

#74

a = input()
a = int(a)

def countdown(item):
    count = item
    for n in range(0, item):
        count = item - n
        print(count)

countdown(a)

#73

a = list(map(int, input().split(" ")))
def printout(items):
    for i in items:
        if i != 0:
            print(i)
        else:
            break;

printout(a)

#72

a = input()
a = int(a)
b = list(map(int, input().split(" ")))

def printoutb(a, b):
    if len(b) == a:
        for i in b:
            print(i)

printoutb(a, b)


#71

a = list(map(int, input().split(" ")))
def printout(a):
    for i in a:
        if i != 0:
            print(i)
        else:
            break

printout(a)


#65

a, b, c = map(int, input().split(" "))
if a % 2 == 0:
    print(a)
if  b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c) 

#66

def isEvenOdd(v):
    if v % 2 == 0:
        print("even")
    else:
        print("odd")

a, b, c = map(int, input().split(" "))
isEvenOdd(a)
isEvenOdd(b)
isEvenOdd(c)

#67

def isPlusMinus(v):
    if v > 0:
        print("plus")
    else:
        print("minus")

def isEvenOdd(v):
    if v % 2 == 0:
        print("even")
    else:
        print("odd")

a = input()
a = int(a)
isPlusMinus(a)
isEvenOdd(a)

#68

def grade(score):
    if score >= 90:
        print("A")
    else:
        if score >= 70:
            print("B")
        else:
            if score >= 40:
                print("C")
            else:
                if score >= 0:
                    print("D")

a = input()
a = int(a)
grade(a)

#69.

def contents(statement):
    if statement == "A":
        print("best!!!")
    elif statement == "B":
        print("good!!!")
    elif statement == "C":
        print("run!")
    elif statement == "D":
        print("slowly~")
    else:
        print("what?")

a = input()
a = str(a)
contents(a)

#70.

def season(month):
    if month in (12, 1, 2):
        print("winter")
    elif month in (3, 4, 5):
        print("spring")
    elif month in (6, 7, 8):
        print("summer")
    elif month in (9, 10, 11):
        print("fall")

a = input()
a = int(a)
season(a)

#1154.

a, b = map(int, input().split(" "))

if a > b:
    print(">")
elif b > a:
    print("<")
elif  a == b:
    print("=")


