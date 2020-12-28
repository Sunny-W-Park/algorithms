### Chapter3. List & Set

### Array O(1) ; Linked Structure O(k)

### append, insert, pop

### 전역변수와 지역변수
### insert, sort, size, replace, delete, merge vs clear

items = []

def insert(pos, elm):
    items.insert(pos, elm)

def sort():
    items.sort()

def size():
    return len(items)

def replace(pos, item):
    items[pos] = item

def delete(pos):
    items.pop(pos)

def merge(lst):
    items.extend(lst)

def clear():
    global items
    #전역변수 선언(items 새로 정의)
    items = []


### Test coding

def display(msg = ""):
    print(msg, size(), items )


### Check outputs

display('파이썬 리스트 테스트')

insert(0, 10)
insert(0, 20)
insert(1, 30)
insert(size(), 40)
insert(2, 50)
display('테스트(삽입 x 5)')

sort()
display('테스트(정렬)')

replace(2, 90)
display('테스트(교체 x 1)')

delete(2)
delete(size()-1)
delete(0)
display('테스트(삭제 x 3)')

lst = [1, 2, 3]
merge(lst)
display('테스트(병합 x 1)')

clear()
display('테스트(초기화)')


### Class coding

class ArrayList:

        def __init__(self):
            self.items = []

        def insert(self, pos, elm):
            self.items.insert(pos, elm)

        def delete(self, pos):
            return self.items.pop(pos)

        def isEmpty(self):
            if len(self.items) == 0:
                return True
            else:
                return False

        def getEntry(self, pos):
            return self.items[pos]

        def size(self):
            return len(self.items)

        def clear(self):
            self.items = []

        def find(self, item):
            return self.items.index(item)

        def replace(self, pos, elm):
            self.items[pos] = elm

        def sort(self):
            self.items.sort()

        def merge(self, lst):
            self.items.extend(lst)

        def display(self, msg = ''):
            print(msg, self.size(), self.items)


### Test coding

s = ArrayList() #리스트 객체 생성

s.display('파이썬 리스트 테스트')

s.insert(0, 10)
s.insert(0, 20)
s.insert(1, 30)
s.insert(s.size(), 40)
s.insert(2, 50)
s.display('테스트(삽입 x 5)')

s.sort()
s.display('테스트(정렬)')

s.replace(2, 90)
s.display('테스트(교체 x 1)')

s.delete(2)
s.delete(size()-1)
s.delete(0)
s.display('테스트(삭제 x 3)')

lst = [1, 2, 3]
s.merge(lst)
s.display('테스트(병합 x 1)')

s.clear()
s.display('테스트(초기화)')














