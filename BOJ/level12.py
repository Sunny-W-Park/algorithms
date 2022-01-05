#10989

n = int(input())

check_list = [0 for _ in range(10001)]

for i in range(n):
    num = int(sys.stdin.readline())
    check_list[num] = check_list[num] + 1

for i in range(10001):
    if check_list[i] != 0:
        for j in range(check_list[i]):
            print(i)        #해당 index(i)를 횟수(j) 만큼 출력

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

