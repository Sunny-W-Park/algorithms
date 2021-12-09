#Level 1 

#2557

print("Hello World!")

#10718

for i in range(2):
    print("강한친구 대한육군")

#10171

print("\
\    /\\\n\
 )  ( ')\n\
(  /  )\n\
 \(__)|\
 ")

#10172

print("\
|\_/|\n\
|q p|   /}\n\
( 0 )\"\"\"\\\n\
|\"^\"`    |\n\
||_/=\\\\__|\n\
")

#1000

a, b = map(int, input().split())
print(a+b)

#1001

a, b = map(int, input().split())
print(a-b)

#10998

a, b = map(int, input().split())
print(a * b)

#1008

a, b = map(int, input().split())
print(a / b)

#10869

a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)

#2588

a = int(input())
b = int(input())
r1 = a * (b // 100)
r2 = a * ((b - (r1 / a * 100)) // 10)
r3 = a * ((b - (r1 / a * 100) - (r2 / a * 10)))
print(int(r3))
print(int(r2))
print(int(r1))
print(a * b)

