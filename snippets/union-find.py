#Union-find

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent([x]))
    return x

#보다 효율적인 find_parent 함수
###

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    elif b > a:
        parent[b] = a

v, e = map(int, input().split()) #v, e = 노드 개수, 간선 개수
parent = [0] * (v+1)

#부모 테이블 초기화
for i in range(1, v+1):
    parent[i] = i

#union 연산 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

#각 원소가 속한 집합 출력
for i in range(1, v+1):
    print(find_parent(parent, i), end = ' ')

#부모 테이블 내용
for i in range(1, v+1):
    print(parent[i], end = ' ')


