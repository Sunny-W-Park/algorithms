#43165. 타겟 넘버

from collections import deque
import sys
input = sys.stdin.readline
numbers = list(map(int, input().split()))
target = int(input())

def solution(numbers, target):
    answer = 0
    q = deque()
    q.append(0)
    for t in range(len(numbers)):
        for _ in range(len(q)):
            x = q.popleft()
            q.append(x + numbers[t])
            q.append(x - numbers[t])
    for i in q:
        if i == target:
            answer += 1
    print(answer)
    return answer

solution(numbers, target)

