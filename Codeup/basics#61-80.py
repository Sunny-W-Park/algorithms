### basics #61-80

#72.

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


