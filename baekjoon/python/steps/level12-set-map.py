#14425

N, M = map(int, input().split())
dict = {}
for _ in range(N):
    s = input()
    if s in dict:
        dict[s] += 1
    else:
        dict[s] = 1

result = 0
for _ in range(M):
    check = input()
    if check in dict:
        result += 1
    else:
        continue

print(result)


