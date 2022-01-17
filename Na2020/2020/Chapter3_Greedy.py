import time

#3-4 1이 될때까지

import time

start = time.time()

n, k = map(int, input().split())
count = 0

while n > 1:
    if n % k == 0:
        n /= k
        count += 1
    else:
        n -= 1
        count += 1

print(count)

end = time.time()
print("---%s seconds ---" % (end-start))


#3-3 숫자 카드 게임


n, m = map(int, input().split())
arr = [[0 for i in range(m)] for j in range(n)]
comp = []
for k in range(n):
    arr[k] = list(map(int, input().split()))
    comp.append(min(arr[k]))
print(max(comp))


#3-2 큰수의 법칙

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse = True)
l = m // k
s = m % k
answer = 0
answer = answer + arr[0] * k * l
answer = answer + arr[1] * s
print(answer)

#3-2 풀이(2)

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

start = time.time()

arr.sort()
l = m // k
s = m % k
answer = 0
answer = answer + arr[-1] * k * l
answer = answer + arr[-2] * s
print(answer)

end = time.time()

print("---%s seconds ---" % (end - start))
#소요시간 반으로 감소


#3-1 거스름돈 문제

pay = int(input())
count = 0
coins = [500, 100, 50, 10]

for coin in coins:
    count += pay//coin
    pay %= coin
    #나눈 나머지를 왼쪽 변수에 할당해준다.

print(count)



