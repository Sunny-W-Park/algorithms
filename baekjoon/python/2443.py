#2443

N = int(input())
length = 2*N-1
while N > 0:
    s_count = 2*N-1
    b_count = (length - s_count)//2
    print(" "*b_count + "*"*s_count)
    N -= 1


