#42626

import bisect
import heapq

scoville = [1, 2, 3, 9, 10, 12]
K = 7

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        if len(scoville) == 0:
            return -1

        if scoville[0] >= K:
            return answer

        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + 2*b)
        answer += 1

solution(scoville, K)


