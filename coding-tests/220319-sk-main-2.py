#2 실패

#case1
arr = ["1","2","4","3","3","4","1","5"]
processes = ["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]

from collections import deque

def solution(arr, processes):
    answer = []
    working_list = deque()
    waiting_list = deque()

    ifWrite_waiting = False
    ifWrite_working = False

    t = 0
    while len(working_list) > 0 or len(processes) > 0:
        t += 1

        for i in processes:
            rw, t1, t2, A, B, C = 0, 0, 0, 0, 0, 0
            if i[0:4] == 'read':
                rw, t1, t2, A, B = i.split(' ')
            if i[0:5] == 'write':
                rw, t1, t2, A, B, C = i.split(' ')
            if int(t1) == t and rw == 'read':
                waiting_list.append(i)
                processes.remove(i)
            if int(t1) == t and rw == 'write':
                waiting_list.append(i)
                ifWrite_waiting = True
                processes.remove(i)

        if ifWrite_working == False and ifWrite_waiting == False:
            for j in waiting_list:
                working_list.append(j)
                waiting_list.remove(j)

        if ifWrite_working == False and ifWrite_waiting == True and len(working_list) == 0:
            for j in waiting_list:
                if j[0:5] == 'Write':
                    working_list.append(j)
                    ifWrite_working = True
                    waiting_list.remove(j)
                    break

        if ifWrite_working == True:
            continue

        for w in working_list:
            rw, t1, t2, A, B, C = 0, 0, 0, 0, 0, 0
            if w[0:4] == 'read':
                rw, t1, t2, A, B = w.split(' ')
            if w[0:5] == 'write':
                rw, t1, t2, A, B, C = w.split(' ')

            if rw == read and (int(t1)+int(t2)-1) == t:
                answer.append(arr[A:B])
                working_list.remove(w)
            if rw == write and (int(t1)+int(t2)-1) == t:
                for s in range(A, B+1):
                    arr[s] = str(C)
                working_list.remove(w)
                ifWrite_working = False

    return answer

solution(arr, processes)


#1 성공

#words = 'abcdef'
#print(words[1:2])

#case1 
goods = ["pencil","cilicon","contrabase","picturelist"]

#case2
goods = ["abcdeabcd","cdabe","abce","bcdeab"]	

def solution(goods):
    answer = []

    length = 0
    key = ''

    for i in goods:
        result = []
        result_string = ''
        while length <= len(i):
            length += 1
            count = 0
            for j in range(0, len(i)):
                if j+length <= len(i):
                    key = i[j:j+length]
                for k in goods:
                    if key in k:
                        count += 1
                if count == 1:
                    result.append(key)
                count = 0
        if len(result) == 0:
            result_string = 'None'
            answer.append(result_string)
        else:
            min_length = len(result[0])
            result_sort = []
            for x in result:
                if len(x) == min_length and (x not in result_sort):
                    result_sort.append(x)
                elif len(x) != min_length:
                    break
            result_sort.sort()
            answer.append(" ".join(result_sort))
        length = 0

    print(answer)
    return answer

#solution(goods)
