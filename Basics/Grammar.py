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












