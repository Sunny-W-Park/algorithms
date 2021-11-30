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
