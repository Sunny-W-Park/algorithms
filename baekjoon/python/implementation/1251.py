#1251

result = []
s = input()

cut = []
for i in range(1, len(s)-1):
    for j in range(i+1, len(s)):
        cut.append([i, j])

for ops in cut:
    br = []
    br.append(s[0:ops[0]])
    br.append(s[ops[0]:ops[1]])
    br.append(s[ops[1]:])
    reverse = []
    for i in range(3):
        new_word = ''
        for j in range(len(br[i])-1, -1, -1):
            new_word += br[i][j]
        reverse.append(new_word)
    result.append(''.join(reverse))

result.sort()
print(result[0])


