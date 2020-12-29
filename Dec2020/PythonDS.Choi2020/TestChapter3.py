### TestChapter3. List and Set


### 3.1
#no coding question


### 3.2

blank = []

def insert(pos, elm):
    blank.insert(pos, elm)
    print(blank)

def size():
    return len(blank)

insert(0, 10)
insert(1, 20)
insert(0, 30)
insert(2, 40)
insert(size(), 50)


### 3.3

def replace(pos, item):
    blank[pos] = item
    print(blank)

def delete(pos):
    blank.pop(pos)
    print(blank)

insert(1, 60)
replace(2, 70)
delete(2)


### 3.4
#no coding question


### 3.5

def findmax(lst):
    maxv = lst[0]
    for i in range(0, len(lst)):
        if maxv < lst[i]:
            maxv = lst[i]

    print(maxv)

lstinput = [20, 39, 29, 10, 90, 84]
findmax(lstinput)


### 3.6

def findmaxmin(lst):
    answer = ()
    dummylst = []
    maxv = lst[0]
    minv = lst[0]
    for i in range(0, len(lst)):
        if maxv < lst[i]:
            maxv = lst[i]

        if minv > lst[i]:
            minv = lst[i]

    dummylst.append(maxv)
    dummylst.append(minv)
    answer = tuple(dummylst)
    print(answer)

findmaxmin(lstinput)


### 3.7

def intersection(lst1, lst2):
    dummylst = []
    for i in lst1:
        if i in lst2:
           dummylst.append(i)

    if len(dummylst) > 0:
        print(True)

    else:
        print(False)

#        if i in lst2:
#            print(True)
#        else:
#            print(False)
#

lstinput2 = [1, 20, 2]
lstinput3 = [1, 2]
intersection(lstinput, lstinput2)
intersection(lstinput, lstinput3)


### 3.8

def sortnmerge(lst1, lst2):
    lst1.sort()
    lst2.sort()
    lst1.extend(lst2)
    lst1.sort()
    print(lst1)

sortnmerge(lstinput, lstinput2)


### 3.9


class Set:
    def __init__(self):
        self.items = []

    def insert(self, elm):
        self.items.append(elm)

    def display(self, msg = ""):
        print(msg, self.items)

    def propersubset(self, setB):
        setDummy = Set()
        setDummy.items = []
        for n in setB.items:
            if n in self.items:
                setDummy.items.append(n)

        if list(setDummy.items) == list(setB.items):
            print("Not Proper Subset")

        else:
            print("Proper Subset")


setA = Set()
setA.insert(0)
setA.insert(1)
setA.display("setA")

setB = Set()
setB.insert(0)
setB.insert(1)
setB.display("setB")

setC = Set()
setC.insert(0)
setC.insert(1)
setC.insert(2)
setC.display("setC")

setA.propersubset(setB)
setA.propersubset(setC)
