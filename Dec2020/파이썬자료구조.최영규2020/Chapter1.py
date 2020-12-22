### Chapter1. Data structure and Algorithm

### Measuring Time Cost

import time

def insert(myBag, e):
    myBag.append(e)

myBag = []
start = time.time()
insert(myBag, "축구공")
end = time.time()
print("실행시간 = ", end-start)


### Identifying odd/even numbers
n = 131
if n%2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")
