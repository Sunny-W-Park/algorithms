#15596

def solve(a: list) -> int:
    ans = 0
    for i in range(len(a)):
        ans += a[i]
    return ans

#4673

natural_num = set(range(1, 10001))
generated_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generated_num.add(i)

result_num = sorted(natural_num - generated_num)

for k in result_num:
    print(k)

#1065 

n = int(input())
list = []

for i in range(1, n+1):
    if 100 > i:
        list.append(i)

    elif 1000 > i >= 100:
        check = []
        for j in range(len(str(i))):
            check.append(int(str(i)[j]))

        if check[2] - check[1] == check[1] - check[0]:
            list.append(i)

print(len(list))

