words = input()
devil = list(input().strip())
angel = list(input().strip())

dp = [[[0, 0] for _ in range(len(devil))] for _ in range(len(words))]

length = len(devil)
for j in range(length):
    if words[0] == devil[j]:
        dp[0][j][0] = 1
    if words[0] == angel[j]:
        dp[0][j][1] = 1

for i in range(1, len(words)):
    for j in range(length):
        if devil[j] == words[i]:
            dp[i][j][0] = sum(dp[i-1][jj][1] for jj in range(j))
        
        if angel[j] == words[i]:
            dp[i][j][1] = sum(dp[i-1][jj][0] for jj in range(j))

answer = 0

for j in range(length):
    answer += sum(dp[-1][j])

print(answer)