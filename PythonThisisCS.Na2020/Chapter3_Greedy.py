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
