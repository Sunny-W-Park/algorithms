#4-4 게임 개발

n, m = map(int, input().split())
a, b, d = map(int, input().split())
arr = [[0 for i in range(m)] for j in range(n)]
for j in range(n):
    arr[j] = list(map(int, input().split()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
arr[a][b] = 2
turn_count = 0
move_count = 1

def turn():
    global d
    d = (d + 3) % 4

while True:
    turn()
    na = a + dx[d]
    nb = b + dy[d]
    if arr[na][nb] == 0:
        a = na
        b = nb
        arr[na][nb] = 2
        move_count += 1
        turn_count = 0
    else:
        turn_count += 1

    if turn_count == 4:
        na = a - dx[d]
        nb = b - dy[d]
        turn_count = 0
        if arr[na][nb] == 0:
            a = na
            b = nb
        if arr[na][nb] == 1 or arr[na][nb] == 2:
            break

print(move_count)


for j in range(n):
    for i in range(m):
        print(arr[i][j], end = ' ')
    print()


#4-3 왕실의 나이트

pos = input()
r = int(pos[1])
c = int(ord(pos[0])) - int(ord('a')) + 1
#아스키코드로 변환하여 좌표 입력

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, -2)]

result = 0
for step in steps:
    newr = r + step[0]
    #x좌표 경우의 수
    newc = c + step[1]
    #y좌표 경우의 수
    if newr >= 1 and newr <= 8 and newc >= 1 and newc <= 8:
        result += 1

print(result)

#4-2 시각

n = int(input())
count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)

#4-1 상하좌우

n = int(input())
command = list(map(str, input().split()))
x, y = 1, 1

for k in range(len(command)):
    p = command[k]
    if n > x  and p == "D":
        x += 1
    elif n > y and p == "R":
        y += 1
    elif x > 1 and p == "U":
        x -= 1
    elif y > 1 and p == "L":
        y -= 1

print(x, y)
