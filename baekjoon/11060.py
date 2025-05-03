N = int(input())
array = [0]
array.extend(list(map(int, input().strip().split())))

inf = int(1e6)

dp = [inf]*(N+1)
dp[N] = 0

for i in range(N-1, 0, -1):
    if i + array[i] >= N: # 바로 점프하면 탈출 가능
        dp[i] = 1
        continue
    
    if array[i] > 0:
        min_val = inf
        for j in range(i+1, min(i+array[i]+1, N+1)):
            if dp[j] != inf:
                min_val = min(min_val, dp[j])
        if min_val != inf:
            dp[i] = min_val + 1

if dp[1] == inf:
    print(-1)
else:
    print(dp[1])