### Chapter5. Queue, BFS

MAX_QSIZE = 10

class CircularQueue:
    def __init__(self):
        self.items = [None] * MAX_QSIZE
        self.front = 0
        self.rear = 0

    def __str__(self):
        return str(self.items)

    def isEmpty(self): return self.front == self.rear

    def isFull(self): return self.front == (self.rear + 1) % MAX_QSIZE

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % MAX_QSIZE
            self.items[self.rear] = item

    def dequeue(self):
        if not self.isEmpty:
            self.front = (self.front + 1) % MAX_QSIZE
            return self.items[self.front]

    def peek(self):
        if not self.isEmpty:
            return self.items[(self.front + 1) % MAX_QSIZE] #선출

    def size(self):
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE
 
    def display(self):
        out = []
        if self.rear - self.front > 0:
            out = self.items[self.front + 1 : self.rear + 1]
        else:
            out = self.items[self.front + 1 : MAX_QSIZE] + self.items[0 : self.rear + 1]

        print("[front = %s, rear = %d] ==> " %(self.front, self.rear), out)


### BFS


mapp = [[0 for i in range(6)] for j in range(6)]
for i in range(6):
    mapp[i] = list(map(str, input().split()))

def isValidPos(x, y):
    if x < 0 or y < 0 or x <= 6 or y <= 6:
        return False
    if mapp[x][y] == 0 or mapp[x][y] == 'x':
        return True

def BFS():
    queue = CircularQueue()
    queue.enqueue( (1, 0) )
    print('BFS: ')
    print(queue)

    while not queue.isEmpty():
        here = queue.dequeue()
        print(here, end = ' -> ')
        (x, y) = here

        if (mapp[x][y] == 'x') : return True

        else:
            mapp[x][y] = '.'
            if isValidPos(x, y-1): queue.enqueue((x, y-1))
            if isValidPos(x, y+1): queue.enqueue((x, y+1))
            if isValidPos(x-1, y): queue.enqueue((x-1, y))
            if isValidPos(x+1, y): queue.enqueue((x+1, y))
    return False

result = BFS()
if result: print(' --> 미로탐색 성공 ')
else: print(' --> 미로탐색 실패 ')
