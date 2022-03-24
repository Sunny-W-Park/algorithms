#10808

S = input()
dp = [0 for i in range(123)]
for i in range(len(S)):
    dp[ord(S[i])] += 1
for i in range(len(dp)):
    if 97 <= i <= 122:
        print(dp[i], end = ' ')



