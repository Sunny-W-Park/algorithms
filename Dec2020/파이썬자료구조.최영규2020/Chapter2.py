### Chapter2. Python Review

###
#Vi copy and paste to another file : " + * + yy(pp for paste)
###


data = [1,2,3,4,5]


### find max

def find_max(a):
    max = a[0]
    for i in range(1, len(a)):
        if max < a[i]: max = a[i]
    return max

print("max = ", find_max(data))


### find min and max

def find_minmax(a):
    max = a[0]
    min = a[0]
    for i in range(1, len(a)):
        if max < a[i]: max = a[i]
        if min > a[i]: min = a[i]
    return max, min

x,y = find_minmax(data)
print("(min,max) = ", (x,y))


### sum of range

def sum_range(begin, end, step = 1):
    sum = 0
    for n in range(begin, end, step):
        sum += n
    return sum

print("sumrange = ", sum_range(1,10))





### sum of range using keyword instances

def sum_range(begin, end, step):
    sum = 0
    for n in range(begin, end, step):
        sum += n
    return sum

print("sumrange*keyword = ", sum_range(1, 10, 1))






