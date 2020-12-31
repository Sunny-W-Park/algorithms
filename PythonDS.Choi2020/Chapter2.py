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
    def __init__(self, color, speed = 0):
        self.color = color
        self.speed = speed

    def speedUp(self): self.speed += 10

    def speedDown(self): self.speed -= 10

    def isEqual(self, carB):
        if self.color == carB.color: return True
        else: return False

    def __str__(self):
        #convert to str
        return "color = %s, speed = %d" %(self.color, self.speed)

car1 = Car('black', 70)
car2 = Car('blue', 60)
car3 = Car('yellow', 50)
car4 = Car('orange')

print("same color? = ", Car.isEqual(car1, car2))
print(car1)
print("[car1]", car1)


### 2.12 super(parent) class

class SuperCar(Car):
    def __init__(self, color, speed = 0, TurboMode = True):
        super().__init__(color, speed) #no need to redefine self.color, self.speed
        self.TurboMode = TurboMode

    def setTurboMode(self, TurboMode = True):
        self.TurboMode = TurboMode

    def speedUp(self): #overriding: re-define function 'speedUp' (which exists in parent class)
        if self.TurboMode:
            self.speed += 50
        else:
            super().speedUp() #parent class method

    def __str__(self):
        if self.TurboMode:
            return "[%s] [speed = %d] Turbo Mode" % (self.color, self.speed)
        else:
            return "[%s] [speed = %d] Normal Mode" % (self.color, self.speed)

s1 = SuperCar('SuperBlack', 170)
s2 = SuperCar('SuperBlue', 160)
s3 = SuperCar('SuperYellow', 150)
s4 = SuperCar('SuperOrange')

print(s1)
print("Lamborghini:", s1)





