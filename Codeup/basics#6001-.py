#6001

print("Hello")

#6002

print("Hello World")

#6003

print("Hello\nWorld")

#6004

print("\'Hello\'")

#6005

print("\"Hello\"")

#6006

print("\"!@#$%^&*()\'")

#6007

print("\"C:\Download\\'hello'.py\"")

#6008

print("print(\"Hello\\nWorld\")")

#6009

a = input(str())
print(a)

#6010

a = input()
print(int(a))

#6011

a = input()
print(float(a))

#6012

a = input()
b = input()
print(a)
print(b)

#6013

a = input()
b = input()
print(str(b))
print(str(a))

#6014

a = input()
print(float(a))
print(float(a))
print(float(a))

#6015

a, b = map(int, input().split(" "))
print(a)
print(b)

#6016

a, b = map(str, input().split(" "))
print(b + " " + a)

#6017

a = input()
print(a, a, a)

#6018

a, b = map(int, input().split(":"))
print(a, b, sep = ":")

#6019

a, b, c = map(int, input().split("."))
print(c, b, a, sep = "-")

#6020

a, b = map(str, input().split("-"))
print(a, b, sep = "")

#6021

a = input()
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

#6022

a = input()
print(a[0]+""+a[1]+" "+a[2]+""+a[3]+" "+a[4]+""+a[5])

#슬라이싱 사용 시

a = input()
print(a[0:2]+" "+a[2:4]+" "+a[4:6])

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

#6024

a, b = map(str, input().split(" "))
print(a+b)

#6025

a, b = map(int, input().split(" "))
print(a+b)

#6026

a = input()
a = float(a)
b = input()
b = float(b)
print(a+b)

#6027

a = input()
a = int(a)
print('%x'% a)

#6028

a = input()
a = int(a)
print('%X'% a)

#6029

a = input()
a = int(a, 16)
print('%o'% a)

#6030

a = ord(input())
print(a)

#6031

a = input()
a = int(a)
print(chr(a))

#6032

a = input()
a = int(a)
print(-a)

#6033

a = input()
a = ord(a)
a = a+1
print(chr(a))

#6034

a, b = map(int, input().split(" "))
print(a-b)

#6035

a, b = map(float, input().split(" "))
print(a*b)

#6036

a, n = input().split(" ")
n = int(n)
print(a*n)

#6037

n = input()
n = int(n)
a = input()
a = str(a)
print(a*n)

#6038

a, b = map(int, input().split(" "))
print(a**b)

#6039

a, b = map(float, input().split(" "))
print(a**b)

#6040

a, b = map(int, input().split(" "))
print(a//b)

#6041

a, b = map(int, input().split(" "))
print(a%b)

#6042

a = input()
a = print(round(float(a), 2))

#6043

a, b = map(float, input().split(" "))
print("{:.3f}".format(a/b))

#6044

a, b = map(int, input().split(" "))
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print("{:.2f}".format(a/b))

#6045

a, b, c = map(int, input().split(" "))
d = a+b+c
e = (a+b+c)/3
print(d, "{:.2f}".format(e))

#6046

a = input()
a = int(a)
print(2*a)

#6047

a, b = map(int, input().split(" "))
c = 2**b
print(a*c)

#6048

a, b = map(int, input().split(" "))
if a < b:
    print("True")
else:
    print("False")

#6049

a, b = map(int, input().split(" "))
if a == b:
    print("True")
else:
    print("False")

#6050

a, b = map(int, input().split(" "))
if b >= a:
    print("True")
else:
    print("False")

#6087

a = int(input())

for i in range(1, a+1):
    if(i%3 == 0):
        continue
    print(i)

#6088

a, d, n = map(int, input().split(" "))

result = a

for i in range(n-1):
    result = result+d

print(result)
