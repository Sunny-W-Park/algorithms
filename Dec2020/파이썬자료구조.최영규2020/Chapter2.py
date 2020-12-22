### Chapter2. Python Review

###
#Vi copy and paste to another file : " + * + yy(pp for paste)
###


data = [1,2,3,4,5]


### 2.7 find max

def find_max(a):
    max = a[0]
    for i in range(1, len(a)):
        if max < a[i]: max = a[i]
    return max

print("max = ", find_max(data))


### 2.8 find min and max

def find_minmax(a):
    max = a[0]
    min = a[0]
    for i in range(1, len(a)):
        if max < a[i]: max = a[i]
        if min > a[i]: min = a[i]
    return max, min

x,y = find_minmax(data)
print("(min,max) = ", (x,y))


### 2.9 sum of range

def sum_range(begin, end, step = 1):
    sum = 0
    for n in range(begin, end, step):
        sum += n
    return sum

print("sumrange = ", sum_range(1,10))


### 2.9+  sum of range using keyword instances

def sum_range(begin, end, step):
    sum = 0
    for n in range(begin, end, step):
        sum += n
    return sum

print("sumrange*keyword = ", sum_range(1, 10, 1))


### 2.10 defining class


class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    car1 = Car('black', 30)
    car2 = Car('yellow', 20)
    car3 = Car('red', 10)
    car4 = Car('blue', )

    def speedUp(self): self.speed += 10

    def speedDown(self): self.speed -= 10

    def isEqual(self, carB):
        if self.color == carB.color : return True
        else : return False


