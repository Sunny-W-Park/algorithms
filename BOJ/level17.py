#5086

a, b = 1, 1
while a!= 0 and b!= 0:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')

#1037

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)

if len(arr) == 1:
    print(arr[0] * arr[0])

else:
    print(arr[0] * arr[-1])

