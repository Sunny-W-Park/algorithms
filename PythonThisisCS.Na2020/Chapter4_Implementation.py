#4-4 게임 개발

n, m = map(int, input().split())
x, y, d = map(int, input().split())
arr = [[0 for i in range(m)] for j in range(n)]
for k in range(n):
    arr[k] = list(map(int, input().split()))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
#북, 동, 남, 서
#좌표 움직이는 연산에 사용 dx[d], dy[d]

count = 1
turn = 0
arr[x][y] = 1
#초기값

while True:
    cd = (d+3) % 4
    #changed direction: 원형 큐 개념 활용
    nx = x + dx[cd]
    ny = y + dy[cd]



    #시작과 동시에 왼쪽으로 90도



    nx = x + dx[d]
    ny = y + dy[d]
    if arr[nx][ny] == 0:
        arr[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
    else:
        turn()
        turn_time += 1
    if turn_time == 4:
    #네 방향 모두 갈 수 없는 경우
        nx = x - dx[d]
        ny = y - dy[d]
        #방향 유지한채로 뒤로 이동
        if arr[nx][ny] == 0:
            arr[nx][ny] = 1
            x = nx
            y = nx
        else:
         break;
        turn_time = 0

print(count)

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
