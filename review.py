#2021.12.16

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

#2021.12.28 

#9020

def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

numbers = list(range(2, 10001))
prime = []
for i in numbers:
    if isPrime(i):
        prime.append(i)

t = int(input())

for i in range(t):
    n = int(input())
    a = 0
    b = 0
    for j in range(len(prime)):
        if prime[j] >= n/2:
            if n - prime[j] in prime:
                b = prime[j]
                a = n - prime[j]
                break
    print(a, b)

