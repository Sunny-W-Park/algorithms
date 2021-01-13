#1173

a, b = map(int, input().split())

def backintime(h, m):
    if h != 0:
        if m >= 30:
            m = m - 30
        else:
            m = 30 - m
            m = 60 - m
            h-= 1
    else:
        if m >= 30:
            m = m - 30
        else:
            m = 30 - m
            m = 60 - m
            h = 23
    print(h, m)

backintime(a, b)

#1172

a = list(map(int, input().split()))
a.sort()
for i in range(len(a)):
    print(a[i], end = ' ')
