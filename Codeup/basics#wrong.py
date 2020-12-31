#basics_wrong questions

#12

a = input()
a = float(a)
print('%f' % a)


#8.
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
print("\u250c\u252c\u2510\n\u251c\u253c\u2524\n\u2514\u2534\u2518")


#15.

a = input()
a = float(a)
a = round(a, 2)
print('%.2f' % a)


#19.

a, b, c = map(int, input().split("."))
print("%02d.%02d.%02d" % (a, b, c))


#45.

a, b = map(int, input().split(" "))
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
c = round(b/a, 2)
print("%.2f" % a)


#57.

a = input()
a = float(a)
if a >= 50:
    if 60 >= a:
        print("win")
    else:
        print("lose")
else:
    print("lose")
