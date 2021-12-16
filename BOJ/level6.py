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


