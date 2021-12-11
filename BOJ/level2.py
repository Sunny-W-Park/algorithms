#1330

a, b = map(int, input().split())
if a > b:
    print(">")
elif a < b:
    print("<")
elif a == b:
    print("==")

#9498

score = int(input())

if 100 >= score >= 90:
    print("A")
elif 89 >= score >= 80:
    print("B")
elif 79 >= score >= 70:
    print("C")
elif 69 >= score >= 60:
    print("D")
else:
    print("F")

#2753

year = int(input())

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("1")
else:
    print("0")

