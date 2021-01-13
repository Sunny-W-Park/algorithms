#3301

n = int(input())
cash = [50000, 10000, 5000,  1000, 500, 100, 50, 10]
count = 0

for c in cash:
    count += n//c
    n %= c

print(count)


#3120 미해결

a, b = map(int, input().split())
button = [1, -1, 5, -5, 10, -10]
c = b-a
if c < 0:
    c = -c
count = 0

button.sort(reverse = True)
for t in button:
    count += c // t
    c %= t
print(count)

#2000

pasta = [0 for i in range(3)]
juice = [0 for j in range(2)]
for i in range(3):
    pasta[i] = int(input())
for j in range(2):
    juice[j] = int(input())

pasta.sort()
juice.sort()

miv = (pasta[0] + juice[0]) * 1.1
print("%.1f" % miv)

