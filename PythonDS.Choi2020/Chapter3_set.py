### Chapter3. List & Set

class Set:
    def __init__(self):
        self.items = []
        #blank list

    def size(self):
        return len(self.items)

    def display(self, msg):
        print(msg, self.items)

    def contains(self, item):
        if item in self.items:
            print(True)
        else:
            print(False)

    def containsreturn(self, item):
        return item in self.items
        #if -> return

    def containsrange(self, item):
        for i in range(0, len(self.items)):
            if self.items[i] == item:
                return True
            else:
                return False

    def insert(self, elm):
        if elm not in self.items:
            self.items.append(elm)

    def delete(self, elm):
        if elm in self.items:
            self.items.remove(elm)


### Functions between sets

    def union(self, setB):
        setA = Set()
        setA.items = list(self.items)
        for elm in setB.items:
            if elm not in setA.items:
                setA.items.append(elm)
        return setA

    def intersect(self, setB):
        setA = Set()
        for elm in setB.items:
            if elm in self.items:
                setA.items.append(elm)
        return setA

    def difference(self, setB):
        setA = Set()
        for elm in setB.items:
            if elm not in self.items:
                setA.items.append(elm)
        return setA


### Test functions

setA = Set()
setA.insert('phone')
setA.insert('wallet')
setA.insert('towel')
setA.display('SetA: ')

setB = Set()
setB.insert('comb')
setB.insert('python')
setB.insert('wallet')
setB.insert('basketball')
setB.display('SetB: ')

setA.union(setB).display('AUB:' )
setA.intersect(setB).display('A^B:')
setA.difference(setB).display('A-B:' )




