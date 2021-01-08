#basics #40-60

###후기

#64

a  = list(map(int, input().split()))
minv = a[0]
for i in range(0, len(a)):
    if a[i] < minv:
        minv = a[i]
print(minv)

#63

a, b = map(int, input().split())
print(a if a>b else b)

#62

a, b = map(int, input().split())
print(a ^ b)

#61

a, b = map(int, input().split())
print(a | b)

#60

a, b = map(int, input().split())
print(a & b)

#59

a = int(input())
print(~(a))


#58

a, b = map(int, input().split())

if a == 0 and b == 0:
    print(1)
else:
    print(0)


#57

a, b = map(int, input().split())

if a == b:
    print(1)
else:
    print(0)

#56

a, b = map(int, input().split())

if a!=b:
    print(1)
else:
    print(0)

#55

a, b = map(int, input().split())

if a or b == 1:
    print(1)
else:
    print(0)

#54

a, b = map(int, input().split())

if a and b == 1:
    print(1)
else:
    print(0)

#53

a = int(input())
if a == 1:
    print(0)
else:
    print(1)


###전기

#40

a = input()
a = int(a)
print(-a)


#42

a, b = map(int, input().split(" "))
print(a//b)


#43

a, b = map(int, input().split(" "))
print(a%b)


#44

a = input()
print(a + 1)


#45

a, b = map(int, input().split(" "))
print(a + b)
print(a - b)
print(a*b)
print(a//b)
print(a%b)
d = round(a/b, 2)
print(d)



#47

a = input()
a = int(a)
print(a*2)


#49-52

a, b = map(int, input().split(""))
if a>b:
    print(1)
else:
    print(0)


#50

a, b = map(int, input().split(" "))
if a==b:
    print(1)
else:
    print(0)



