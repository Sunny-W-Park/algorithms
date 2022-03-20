#2444

N = int(input())
t = 0
length = 2*N-1
while(t < N):
    t += 1
    s_count = 2*t-1
    b_count = (length-s_count)//2
    print(' '*b_count + '*'*s_count)
while(t > 1):
    t -= 1
    s_count = 2*t-1
    b_count = (length-s_count)//2
    print(' '*b_count + '*'*s_count)


