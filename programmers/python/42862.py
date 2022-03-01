#42862

n = 5
lost = [2, 4]
reserve = [1, 3, 5]


def solution(n, lost, reserve):
    answer = 0

    n_reserve = []
    n_lost = []

    for i in reserve:
        if i not in lost:
            n_reserve.append(i)

    for i in lost:
        if i not in reserve:
            n_lost.append(i)

    n_reserve = sorted(n_reserve)
    n_lost = sorted(n_lost)

    found = []
    for i in n_lost:
        for j in n_reserve:
            if i+1 == j or i-1 == j:
                found.append(i)
                n_reserve.remove(j)

    answer += n - len(n_lost) + len(found)

    return answer


