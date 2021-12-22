#1712

a, b, c = map(int, input().split())

q = 0

if b >= c:
    q = -1

else:
    q = a // (c-b) + 1

print(q)

#2292

n = int(input())

i = 0
start = 1
end = 1

while True:
    if end >= n >= start:
        print(i+1)
        break
    else:
        i = i+1
        start = end + 1
        end = end + 6 * i

#1193

x = int(input())

index_start = 1
index_end = 1
d = 1

while True:
    if index_end >= x >= index_start:
        break
    else:
        index_start = index_start + d
        d = d + 1
        index_end = index_end + d

index = x - index_start
a = 1
b = d
a = a + index
b = b - index

if d % 2 == 0:
    print(str(a) + "/" + str(b))

else:
    print(str(b) + "/" + str(a))

#2869

import math

a, b, v = map(int, input().split())
x = (v - b) / (a - b)
x_ceil = math.ceil(x)
print(x_ceil)

