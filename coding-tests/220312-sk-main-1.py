#2-2

#case1
n = 5
clockwise = True

#case2
n = 6
clockwise = False

#case2
n = 9
clockwise = False

def solution(n, clockwise):
    answer = [[]]
    answer = [[0 for _ in range(n)] for _ in range(n)]
    cwx = [0, 1, 0, -1]
    cwy = [1, 0, -1, 0]
    ctx = [1, 0, -1, 0]
    cty = [0, 1, 0, -1]
    start = [(0, 0), (n-1, n-1), (n-1, 0), (0, n-1)]
    d = 0

    for i in range(4):
        l = n-2
        x, y = start[i][0], start[i][1]
        answer[x][y] = 1
        if clockwise == True:
            if i == 0:
                d = 0
            elif i == 1:
                d = 2
            elif i == 2:
                d = 3
            elif i == 3:
                d = 1
        if clockwise == False:
            if i == 0:
                d = 0
            if i == 1:
                d = 2
            if i == 2:
                d = 1
            if i == 3:
                d = 3

        while l > 0:
            for j in range(l):
                nx, ny = 0, 0
                if clockwise == True:
                    nx = x + cwx[d]
                    ny = y + cwy[d]
                if clockwise == False:
                    nx = x + ctx[d]
                    ny = y + cty[d]
                if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                    if answer[nx][ny] == 0:
                        answer[nx][ny] = answer[x][y] + 1
                        x = nx
                        y = ny
            d += 1
            if d == 4:
                d = 0
            if l == n-2:
                l -= 1
            elif 2 < l < n-2:
                l -= 2
            elif l <= 2:
                l -= 1

    for i in range(n):
        for j in range(n):
            print(answer[i][j], end = ' ')
        print()

    #if clockwise == False
    return answer

solution(n, clockwise)

#2-1

#case1
#n = 5
#clockwise = True
#
##def cd():
##    global d
##    d += 1
##    if d == 4:
##        d = 0
#
#def solution(n, clockwise):
#    answer = [[]]
#
#    answer = [[0 for _ in range(n)] for _ in range(n)]
#
#    cwx = [0, 1, 0, -1]
#    cwy = [1, 0, -1, 0]
#
#    ctx = [1, 0, -1, 0]
#    cty = [0, 1, 0, -1]
#
#    start = [(0, 0), (n-1, n-1), (n-1, 0), (0, n-1)]
#    d = 0
#
#    if clockwise == True:
#        for i in range(4):
#            l = n-1
#            x, y = start[i][0], start[i][1]
#            answer[x][y] = 1
#            if i == 0:
#                d = 0
#            elif i == 1:
#                d = 2
#            elif i == 2:
#                d = 3
#            elif i == 3:
#                d = 1
#
#            while l != 0:
#                for j in range(l-1):
#                    print(i, x, y, d)
#                    nx = x + cwx[d]
#                    ny = y + cwy[d]
#                    if 0 <= nx <= n-1 and 0 <= ny <= n-1:
#                        if answer[nx][ny] == 0:
#                            answer[nx][ny] = answer[x][y] + 1
#                            x = nx
#                            y = ny
#                d += 1
#                if d == 4:
#                    d = 0
#                l -= 1
#
#    for i in range(n):
#        for j in range(n):
#            print(answer[i][j], end = ' ')
#        print()
#
#    #if clockwise == False
#    return answer
#
#solution(n, clockwise)
#

#1

#case1
#money = 1999
#costs = [2, 11, 20, 100, 200, 600]

#case2
#money = 4578
#costs = [1, 4, 99, 35, 50, 1000]	

def solution(money, costs):
    answer = 0

    coins = [1, 5, 10, 50, 100, 500]
    costs[0] = costs[0]
    costs[1] = min(costs[1], costs[0]*5)
    costs[2] = min(costs[2], costs[1]*2)
    costs[3] = min(costs[3], costs[2]*5)
    costs[4] = min(costs[4], costs[3]*2)
    costs[5] = min(costs[5], costs[4]*5)

    q = [0 for _ in range(6)]
    while money != 0:
        for i in range(5, -1, -1):
            qi = money//coins[i]
            q[i] += qi
            money -= coins[i]*qi

    for i in range(6):
        answer += costs[i]*q[i]

    return answer

solution(money, costs)
