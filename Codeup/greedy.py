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

