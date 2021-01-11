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

def peek():
    if not isEmpty():
        return top[-1]

def size():
    return len(top)

def clear():
    global top
    top = []


### Class exercise

class Stack:
    def __init__(self):
        self.top = []

    def __str__(self): #stack -> str
        return str(self.top)

    def isEmpty(self):
        return len(self.top) == 0

    def push(self, item):
        return self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]

    def size(self):
        return len(self.top)

    def clear(self):
        self.top = []

### Odds, Evens

odd = Stack()
even = Stack()

for i in range(10):
    if i%2 == 0:
        even.push(i)
    else:
        odd.push(i)

print(odd)
print(even)

print(odd.peek())
print(even.peek())

for _ in range(2):
    even.pop()

for _ in range(3):
    odd.pop()

print(odd.top)
print(even.top)


### Checking brackets with Stack

def checkbrackets(statement):
    stack = Stack()
    for ch in statement:
        if ch in ('(', '[', '{'):
            stack.push(ch)

        elif ch in (')', ']', '}'):
            if stack.isEmpty():
                return False

            else:
                left = stack.pop()
                if (ch == ')' and left!= '(') or \
                   (ch == ']' and left!= '[') or \
                   (ch == '}' and left!= '{'):
                        return False
#                else:
#                       return True
#삭제 이유(중요): stack.isEmpty()로 남아있는 요소 검증해야함

    return stack.isEmpty()

### inputs

statements = ("{A[(i+1)]} = 0;", "if((i==0) && (j==0)", "A[(i+1]) = 0;")
for s in statements:
    m = checkbrackets(s)
    print(s, "---->", m)


### Postfix Calculator using Stack

def evalPostfix(expr):
    stack = Stack()
    for elm in expr:
        if elm in ('+', '-', '*', '/'):
            v2 = stack.pop()
            v1 = stack.pop()
            if (elm  == '+'): stack.push(v1 + v2)
            elif (elm == '-'): stack.push(v1 - v2)
            elif (elm == '*'): stack.push(v1 * v2)
            elif (elm == '/'): stack.push(v1 / v2)
        else:
            stack.push(float(elm))

    return stack.pop()
    #print the last elm


expr1 = ['8', '2', '/', '3', '-', '3', '2', '*', '+']
expr2 = ['1', '2', '/', '4', '*', '1', '4', '/', '*']
print(expr1, '----->', evalPostfix(expr1))
print(expr2, '----->', evalPostfix(expr2))


def precedence(op):
    if (op == '(' or op == ')'): return 0
    elif (op == '+' or op == '-'): return 1
    elif (op == '*' or op == '/'): return 2
    else: return -1


















