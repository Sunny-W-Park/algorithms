#2750
#2750

n = int(input())
list = []

for i in range(n):
    list.append(int(input()))

list.sort()

for i in range(n):
    print(list[i])

#2751

n = int(input())
list = []

for i in range(n):
    list.append(int(input()))

for i in sorted(list):
    print(i)

