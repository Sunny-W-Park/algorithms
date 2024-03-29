#1. 자료형
#1.1 수 자료형: 정수형, 실수형

#실수형
a = 1e9        #지수 표현 방식
print(a)

a = 3954e-3
print(a)

#round 연산
a = round(a, 2)
print(a)


#1.2 리스트 자료형

#리스트 초기화
n = 10        #크기가 n이고, 모든 값이 0인 1차원 리스트 초기화
a = [0] * n
print(a)

#인덱싱: 인덱스값을 입력하여 리스트의 특정한 원소에 접근

#슬라이싱: 연속적인 위치를 갖는 원소들에 접근

#리스트 컴프리헨션

array = [i for i in range(20) if i % 2 == 1]         #0부터 19까지의 수 중에서 홀수만 포함하는 리스트
print(array)

#일반화

array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)
print(array)

#2차원 리스트 컴프리헨션

n = 3
m = 3        #N X M 크기의 2차원 리스트 초기화
array = [[0] * m for _ in range(n)]        #반복을 위한 변수를 무시하고자 할때 언더바(_) 사용
print(array)

#리스트 관련 기타 메서드

#append(), sort(), reverse(), insert(), count(), remove()

#remove 활용: 특정한 값의 원소를 모두 제거

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = [3, 5]        #dict, list 모두 가능
a = [i for i in a if i not in remove_set]
print(a)


#1.3 문자열 자료형
print("Hello World")
print("\"Hello World\"")

#문자열 연산
a = "Hello"
b = "World"
print(a + "" + b)
print(a*3)
print(a[2:4])


#1.4 튜플 자료형
#*튜플은 한 번 선언된 값을 변경할 수 없음, 원소의 대입 불가
#*리스트는 대괄호([])를 이용, 튜플은 소괄호(())를 이용


#1.5 사전 자료형
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['키위'] = 'Kiwi'
print(data)

#사전 자료형 관련 함수
key_list = data.keys()
print(key_list)
value_list = data.values()
print(value_list)

for key in key_list:
    print(data[key])


#1.6 집합 자료형
#*중복을 허용하지 않음
#*순서가 없음

#집합 자료형의 연산
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])
print(a | b)        #합집합
print(a & b)        #교집합
print(a - b)        #차집합

#집합 자료형 관련 함수
#*add: 새로운 원소 추가 (시간 복잡도 O(1))
#*update: 새로운 원소 여러 개 추가
a.update(["a", "b"])
print(a)
#*remove: 특정 값을 갖는 원소 삭제 (시간 복잡도 O(1))
a.remove(1)
print(a)


#2. 조건문

a = 48
if a >= 90:
    print("A")
elif a >= 80 and a < 90:
    print("B")
elif a >= 70 and a < 80:
    print("C")
else: 
    print("F")

#pass문

a = 85
if a >= 80:
    pass
else:
    print("성적이 80점 미만입니다.")
print("프로그램을 종료합니다.")


#3. 반복문

#3.1 While문

i = 1
result = 0
while i <= 9:
    result += i
    i += 1
print(result)

i = 1
result = 0
while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1
print(result)


#3.2 For문

result = 0
for i in range(10):
    result += i
print(result)

#continue

scores = [1, 2, 3, 4, 5]
cheating_list = {2, 4}
for i in range(5):
    if i+1 in cheating_list:
        continue
    if scores[i] >= 3:
        print(i+1, "번 학생은 합격입니다")

#구구단 출력

for i in range(1, 10):
    for j in range(1, 10):
        print(i, "X", j, "=", i*j)
    print()


#4. 함수

#global 키워드 변수 저장

a = 0

def func():
    global a        #global 없을시 func() 함수에서 변수 인식 불가
    a += 1

for i in range(10):
    func()

print(a)


#5. 입출력

#sys 라이브러리, 데이터 입력 속도 up
import sys
data = sys.stdin.readline().rstrip()
print(data)


#6. 주요 라이브러리의 문법과 유의점

#6.1 내장함수
#대표적인 내장함수: sum(), input(), print(), min(), max(), eval(), sorted() 등 별도의 import 없이 사용 가능
#리스트와 같은 iterable 객체는 기본으로 sort() 함수를 내장

#6.2 itertools
#permutation
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)

#combination
from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result)

