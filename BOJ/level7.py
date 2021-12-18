#11654

n = input()
print(ord(n))

#11720

p = input()
q = input()
list = []

for i in range(len(str(q))):
    list.append(int(q[i]))

print(sum(list))

#10809

s = str(input())

list = [-1 for _ in range(123)]

for i in range(len(s)):
    for j in range(97, 123):
        if chr(j) == s[i]:
            if list[j] == -1:
                list[j] = i

for k in range(97, 123):
    print(list[k], end = ' ')

#2675

t = int(input())

array = []

for _ in range(t):
    array.append(list(input().split()))

for i in range(t):
    array[i][0] = int(array[i][0])
    array[i][1] = str(array[i][1])

for i in range(t):
    result = ''
    for p in range(len(array[i][1])):
        result = result + str(array[i][1][p]) * array[i][0]
    print(result)

#1157

s = str(input()).lower()

list = [0 for _ in range(123)]

for i in range(len(s)):
    for j in range(97, 123):
        if chr(j) == s[i]:
            list[j] += 1

max = 0
result = []

for k in range(123):
    if list[k] > max:
        max = list[k]

for k in range(123):
    if list[k] == max:
        result.append(chr(k))

if len(result) > 1:
    print("?")

elif len(result) == 1:
    print(result[0].upper())


