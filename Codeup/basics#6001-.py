#6001

print("Hello")

#6002

print("Hello World")

#6003

print("Hello\nWorld")

#6010

#a = map(int, input())
#print(a)

a = input()
print(int(a))

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
