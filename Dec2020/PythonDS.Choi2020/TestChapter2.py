### TestChapter2. Python Review

### 2.1

dan = int(input("구구단 단 입력: "))
for i in range(1, 10):
    print(i*dan)


### 2.2 Coding 2.1 using while

dan = int(input("구구단 단 입력:"))
n = 1
while n < 10:
    print("%2d x %2d = " %(dan, n), dan*n)
    n += 1


### 2.3 Coding 2.1 in reverse order

dan = int(input("구구단 단 입력(역순): "))

for i in range(9, 0, -1):
    print(i*dan)


### 2.4 Celcius to Farenheit

Cel = int(input("Celcius?:"))
print("%dCelcius to Farenheit: %d" %(Cel, 32+Cel*180/100))


### 2.5 Farenheit to Celcius

Far = int(input("Farenheit?: "))
print("%dFarenheit to Celcius: %d" %(Far, (Far-32)*100/180))


### 2.6 Reverse list (with negative index only)

A = [1, 2, 3, 4]

for i in range(-len(A), 0):
    print(A[-5-i])


### 2.7 Sum List Values

def listsum(data):
    sum = 0
    for n in data:
        sum += n
    print(sum)

listsum(A)


### 2.8 Convert to Upper/Lower Case letters

msg = "Data Structures in Python"

print(msg)
print(msg.upper())
print(msg.lower())


### 2.9 Dictionary

price = {'콩나물해장국': 4500, '갈비탕': 9000, '돈가스': 8000}
price.update({'팟타이': 7000})
print(price)


### 2.10 Lower price -500 from menu in 2.9



### 2.11 Cumulative Sum

def SumRange(n):
    sum = 0
    for k in range(1, n+1):
        sum += k
    return sum

print(SumRange(10))


### 2.12 Cumulative Sum(2)

def SumRangeN(n):
    sum = 0
    for k in range(1, n+1):
        sum += 1/k
    return sum

print(SumRangeN(10))


### 2.15 define reverse()

def reverse(data):
    output = ''
    for char in data:
        output = char + output

    print(output)

reverse("ABCDE")


### 2.16 printNum & printRevNum

def printNum(n):
    for k in range(1, n+1, 1):
        print(k)

def printRevNum(n):
    for k in range(n, 0, -1):
        print(k)

printNum(10)
printRevNum(10)


















