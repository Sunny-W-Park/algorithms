#1715

import heapq

N = int(input())

cards = []
for _ in range(N):
    cards.append(int(input()))
heapq.heapify(cards)
result = 0

while len(cards) != 1:
    num1 = heapq.heappop(cards)
    num2 = heapq.heappop(cards)
    add = num1 + num2
    result += add
    heapq.heappush(cards, add)

print(result)

