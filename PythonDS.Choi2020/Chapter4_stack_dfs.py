### Chapter4. Stack, DFS

arr = []

class Stack():
    def __init__(self):
        self.arr = []

    def __str__(self):
        return str(self.arr)

    def isEmpty(self):
        return len(self.arr) == 0

    def push(self, item):
        return self.arr.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.arr.pop(-1)

    def peek(self):
        if not self.isEmpty():
            return self.arr[-1]

    def size(self):
        return len(self.arr)

    def clear(self):
        self.arr = []

### DFS 미로찾기

mapp = [[_ for i in range(6)] for _ in range(6)]
for k in range(6):
    mapp[k] = list(map(str, input().split()))

print(mapp)

def isValidPos(x, y):
    if x < 0 or y < 0 or x >= 6 or y >= 6:
        return False
    else:
        return mapp[x][y] == '0' or mapp[x][y] == 'x'

def DFS():
    stack = Stack()
    stack.push( (0, 1) )
    print('DFS:' )

    while not stack.isEmpty():
        here = stack.pop()
        print(here, end = '->')
        (x, y) = here

        if (mapp[x][y] == 'x'):
            return True

        else:
            mapp[x][y] = '.'
            if isValidPos(x, y-1): stack.push((x, y-1))
            if isValidPos(x, y+1): stack.push((x, y+1))
            if isValidPos(x-1, y): stack.push((x-1, y))
            if isValidPos(x+1, y): stack.push((x+1, y))
        print(' 현재 스택: ', stack)
    return False

result = DFS()
if result: print(' --> 미로탐색 성공')
else: print(' --> 미로탐색 실패')


