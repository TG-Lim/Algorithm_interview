N = int(input())

inf = int(1e9)

parent = [0]*(N+1) # 어디 수에서 변화했는 지. parent[2] = 3 이면 2는 3에서 변화되어 옴
dp = [inf]*(N+1) # dp[i]: N에서 i까지 변화했을 때 최소 변환 횟수

dp[N] = 0 # 초기는 0으로 설정
parent[N] = 0

for i in range(N, 0, -1):
    if i % 3 == 0: # 3으로 나누어 떨어짐
        if dp[i] + 1 < dp[i//3]: # 경우의 수 더 작음
            dp[i//3] = dp[i]+1
            parent[i//3] = i
    if i % 2 == 0:
        if dp[i] + 1 < dp[i//2]:
            dp[i//2] = dp[i] + 1
            parent[i//2] = i

    if dp[i] + 1 < dp[i-1]:
        dp[i-1] = dp[i] + 1
        parent[i-1] = i

print(dp[1])
num = 1
paths = ['1']
while num < N:
    paths.append(str(parent[num]))
    num = parent[num]

print(' '.join(paths[::-1]))