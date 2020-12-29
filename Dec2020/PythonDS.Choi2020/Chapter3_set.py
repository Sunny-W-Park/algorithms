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

    def insert(self, pos, elm):
        if elm not in self.items:
            self.items.append(elm)

    def delete(self, elm):
        if elm in self.items:
            self.items.remove(elm)

### Functions between sets

    def union(self, setB):
        setC = Set()
        setC.items = list(self.items)
        for elm in setB.items:
            if elm not in self.items:
                setC.items.append(elm)
        return setC

    def intersect(self, setB):
        setC = Set()
        setC.items = [] #unnecessary 
        for elm in setB.items:
            if elm in self.items:
                setC.items.append(elm)
        return setC

    def difference(self, setB):
        setC = Set()
        setC.items = []
        for elm in setB.items:
            if elm not in self.items:
                setC.items.append(elm)
        return setC

