import time

#3-3 숫자 카드 게임

start = time.time()


end = time.time()
print("---%s seconds ---" % (end-start))



#3-2 큰수의 법칙

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

start = time.time()

arr.sort(reverse = True)
l = m // k
s = m % k
answer = 0
answer = answer + arr[0] * k * l
answer = answer + arr[1] * s
print(answer)

end = time.time()

print("---%s seconds ---" % (end - start))


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

start = time.time()

pay = int(input())
count = 0
coins = [500, 100, 50, 10]

for coin in coins:
    count += pay//coin
    pay %= coin
    #나눈 나머지를 왼쪽 변수에 할당해준다.

print(count)

end = time.time()
print("---%s seconds ---" % (end-start))


