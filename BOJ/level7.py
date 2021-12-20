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

#1152

words = input().split()
print(len(words))

#2908

a, b = map(str, input().split())
list = []
a_reverse = a[2]+a[1]+a[0]
b_reverse = b[2]+b[1]+b[0]
list.append(a_reverse)
list.append(b_reverse)

print(max(list))

#5622

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
results = 0

s = str(input())

for i in range(len(s)):
     for j in range(len(dial)):
         for k in range(len(dial[j])):
             if dial[j][k] == s[i]:
                 results += j+3

print(results)

#2941

s = str(input())
words = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0

for i in range(len(s)):
    if len(s)-1 > i:
        for j in range(len(words)):
            if s[i]+s[i+1] == words[j]:
                count += 1
    if len(s)-2 > i:
        for j in range(len(words)):
            if s[i]+s[i+1]+s[i+2] == words[j]:
                count += 1

print(len(s) - count)

#1316

n = int(input())
words = []
result = 0

for _ in range(n):
    words.append(str(input()))

words_shorten = []
for i in range(n):
    s = ''
    for j in range(len(words[i])):
        if j == 0:
            s = s + words[i][j]
        else:
            if words[i][j] != s[-1]:
                s = s + words[i][j]
    words_shorten.append(s)

for p in range(len(words_shorten)):
    checker = set()
    for q in range(len(words_shorten[p])):
        checker.add(words_shorten[p][q])
    if len(checker) == len(words_shorten[p]):
        result += 1

print(result)



