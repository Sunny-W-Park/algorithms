### Chapter5. Queue

items = []

def isEmpty():
    return len(items) == 0

def enqueue(item):
    items.append(item)

def dequeue(item):
    #delete from the front
    if not isEmpty():
        return items.pop(0)

def peek():
    if not isEmpty():
        return items[-1]

#Circular Queue

MAX_QSIZE = 10 

class CircularQueue :
    def __init__(self):
        self.front = 0 #position
        self.rear = 0
        self.items = [None] * MAX_QSIZE

    def isEmpty(self): return self.front == self.rear

    def isFull(self): return self.front == (self.rear + 1) % MAX_QSIZE

    def clear(self): self.front = self.rear

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % MAX_QSIZE
            self.items[self.rear] = item #important: insert in rear position

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % MAX_QSIZE
            return self.items[self.front] #important: no need to pop, cuz items are inserted at rear

    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front + 1) % MAX_QSIZE]

    def size(self):
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE

    def display(self):
        out = []
        if self.rear > self.front:
            out = self.items[self.front + 1 : self.rear + 1]
        else:
            out = self.items[self.front + 1 : MAX_QSIZE] + self.items[0: self.rear + 1]

        print("[front = %s, rear = %d] ==> " %(self.front, self.rear), out)

items = [None, None, 'b', 'c', 'd', None, None, None]

q = CircularQueue()

for i in range(8): q.enqueue(i)
q.display()

for i in range(5): q.dequeue()
q.display()

for i in range(8, 14): q.enqueue(i)
q.display()
