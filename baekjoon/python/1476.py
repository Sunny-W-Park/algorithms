#1476

E, S, M = map(int, input().split())
E_start, S_start, M_start = 1, 1, 1
count = 1

while (E_start != E) or (S_start != S) or (M_start != M):
    count += 1
    E_start += 1
    if E_start == 16:
        E_start = 1
    S_start += 1
    if S_start == 29:
        S_start = 1
    M_start += 1
    if M_start == 20:
        M_start = 1

print(count)

