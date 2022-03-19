#2445

N = int(input())
s_count = 0
while s_count < N:
    s_count += 1
    b_count = 2*N - 2*s_count
    print('*'*s_count + ' '*b_count + '*'*s_count)
while s_count > 1:
    s_count -= 1
    b_count = 2*N - 2*s_count
    print('*'*s_count + ' '*b_count + '*'*s_count)


