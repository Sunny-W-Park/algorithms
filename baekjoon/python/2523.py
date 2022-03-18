#2523

N = int(input())
length = 0
while(length < N):
    length += 1
    print('*' * length)
while(length > 1):
    length -= 1
    print('*' * length)

