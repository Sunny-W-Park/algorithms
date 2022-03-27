#5

#TC1


abilities = [2, 8, 3, 6, 1, 9, 1, 9]	
k = 2

#TC2

abilities = [7, 6, 8, 9, 10]
k = 1

def solution(abilities, k):
    answer = 0

    if len(abilities) % 2 != 0:
        abilities.append(0)

    diff = []    
    abilities.sort(reverse = True)
    for i in range(0, len(abilities), 2):
        diff.append((abilities[i]-abilities[i+1], i//2))
    diff.sort(reverse = True)

    for i in range(0, len(abilities), 2):
        if k > 0:
            if i//2 == diff[0][1]:
                answer += abilities[i]
                del diff[0]
                k -= 1
            else:
                answer += abilities[i+1]
        else:
            answer += abilities[i+1]

    print(answer)
    return answer

solution(abilities, k)

#3

#TC1

num_teams = 3
remote_tasks = ["development","marketing","hometask"]	
office_tasks = ["recruitment","education","officetask"]	
employees = ["1 development hometask","1 recruitment marketing","2 hometask","2 development marketing hometask","3 marketing","3 officetask","3 development"]

from collections import deque

def solution(num_teams, remote_tasks, office_tasks, employees):
    answer = []

    teams = [[] for _ in range(num_teams+1)]
    remotes = []
    e = []
    for i in employees:
        j = i.split(" ")
        e.append(j)

    for i in range(len(e)):
        teams[int(e[i][0])].append(i+1)
        if_remote = True
        for j in range(1, len(e[i])):
            if e[i][j] not in remote_tasks:
                if_remote = False

        if if_remote == True:
            remotes.append(i+1)

    for p in teams:
        check_all = True
        re = deque()
        for q in p:
            if q in remotes:
                re.append(q)
            if q not in remotes:
                check_all = False
        if len(re) > 0 and check_all == True:
            re.popleft()
            answer.extend(re)
        else:
            answer.extend(re)

    return answer

solution(num_teams, remote_tasks, office_tasks, employees)


#2

#TC1

sentences = ["line in line", "LINE", "in lion"]	
n = 5
result = 20 

#TC2

sentences = ["line in line", "LINE", "in lion"]	 
n = 7

#TC3

sentences = ["ABcD", "bdbc", "a", "Line neWs"]	
n = 5

def solution(sentences, n):
    answer = -1

    s = []
    check_noans = True

    for i in sentences:
        dict = {'shift':0}
        for j in i:
            if j == ' ':
                continue
            if j in dict:
                if j.isupper() == True:
                    dict[j.lower()] += 1
                    dict['shift'] += 1
                else:
                    dict[j] += 1
            else:
                if j.isupper() == True:
                    dict[j.lower()] = 1
                    dict['shift'] += 1
                else:
                    dict[j] = 1

        if dict['shift'] == 0:
            del dict['shift']

        if len(dict) <= n:
            check_noans = False

        s.append(dict)

    for i in s:
        comps = 0
        ins = list(i.keys())
        for j in sentences:
            check_match = True
            for k in j:
                if k.isupper() == True:
                    if k.lower() in ins:
                        comps += 2
                    elif k.lower() not in ins:
                        comps = 0
                        check_match = False
                        break
                else:
                    if k in ins:
                        comps += 1
                    elif k == ' ':
                        comps += 1
                    elif k.lower() not in ins:
                        comps = 0
                        check_match = False
                        break
            if check_match == False:
                continue
            answer = max(answer, comps)

    print(answer)
    return answer

solution(sentences, n)
