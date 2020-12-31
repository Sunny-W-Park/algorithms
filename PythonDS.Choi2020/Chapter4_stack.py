### Chapter4. Stack

### isEmpty, push, pop

top = [] #상단이 열려있다고 가정

def isEmpty():
    return len(top) == 0

def push(item):
    top.append(item)

def pop():
    if not isEmpty():
        return top.pop(-1)

