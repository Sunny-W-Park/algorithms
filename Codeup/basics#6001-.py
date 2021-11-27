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
