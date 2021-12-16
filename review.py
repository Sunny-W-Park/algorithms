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

