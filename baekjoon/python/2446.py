#2446

N = int(input())
s_count = N
length = 2*N-1

while(s_count > 1):
    b_count = (length - (2*s_count-1))//2
    print(' '*(b_count) + '*'*(2*s_count-1))
    s_count -= 1
while(s_count <= N):
    b_count = (length - (2*s_count-1))//2
    print(' '*(b_count) + '*'*(2*s_count-1))
    s_count += 1


