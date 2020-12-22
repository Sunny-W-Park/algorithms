### TestChapter2. Python Review

### 2.1

n = 6
for i in range(1, 10):
    print("구구단 6단 = ", n*i )

for i in range(1, 10):
    print(i*n)


### 2.2 Coding 2.1 using while



### 2.3 Coding 2.1 in reverse order

for i in range(9, 0, -1):
    print(i*n)


### 2.4 Celcius to Farenheit

def CeltoFar(C):
    F = 32+C*180/100
    print(F)

CeltoFar(10)

### 2.5 Farenheit to Celcius


### 2.6 Reverse list (with negative index only)


### 2.7 Sum List Values


### 2.8 Convert to Upper/Lower Case letters


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


### 2.16 printNum & printRevNum

def printNum(n):
    for k in range(1, n+1, 1):
        print(k)

def printRevNum(n):
    for k in range(n, 0, -1):
        print(k)

printNum(10)
printRevNum(10)




















