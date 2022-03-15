#4673 재풀이: 메모이제이션

dp = [0 for _ in range(100000)]

for i in range(1, 10001):
    if 1 <= i < 10:
        x = i + i
        dp[x] = 1
    if 10 <= i < 100:
        x = i + int(str(i)[-2]) + int(str(i)[-1])
        dp[x] = 1
    if 100 <= i < 1000:
        x = i + int(str(i)[-3]) + int(str(i)[-2]) + int(str(i)[-1])
        dp[x] = 1
    if 1000 <= i < 10000:
        x = i + int(str(i)[-4]) + int(str(i)[-3]) + int(str(i)[-2]) + int(str(i)[-1])
        dp[x] = 1
    if i == 10000:
        x = 10001
        dp[x] = 1

for i in range(1, 10001):
    if dp[i] == 0:
        print(i)

#4673

natural_num = set(range(1, 10001))
generated_num = set()
#set 자료형의 특징
#1) 순서 없음 -> sort로 정렬 필요
#2) 중복 없음 -> 데이터 입력시 중복을 차단해주는 역할 수행

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generated_num.add(i)

result_num = sorted(natural_num - generated_num)

for k in result_num:
    print(k)

