#1420

n = int(input()) 
arr = [[0 for m in range(n)] for l in range(n)]
newarr = [[0 for m in range(n)] for l in range(n)]

for i in range(n):
    arr[i] = list(map(str, input().split()))

for j in range(n):
    arr[j][1] = int(arr[j][1])

for k in range(n):
    newarr[k][0] = arr[k][1]
    newarr[k][1] = arr[k][0]

newarr.sort()
print(newarr[-3][1])



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
