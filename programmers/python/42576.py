#42576

def solution(participant, completion):
    dict = {}
    for name in participant:
        if dict.get(name):
            dict[name] += 1
        else:
            dict[name] = 1

    for name in completion:
        dict[name] -= 1

    for key in dict:
        if dict[key] > 0:
            return key

