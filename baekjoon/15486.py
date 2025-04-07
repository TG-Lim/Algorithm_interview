import sys
input = sys.stdin.readline

N = int(input())
time_array = [0]
cost_array = [0]

for i in range(N):
    t, p = map(int, input().strip().split())
    time_array.append(t)
    cost_array.append(p)

dp = [0]*(N+2)

for i in range(N, 0, -1):
    end_day = i + time_array[i]

    if end_day <= N+1:
        dp[i] = max(dp[i+1], cost_array[i] + dp[end_day]) # 상담 안함, 상담 진행
    else:
        dp[i] = dp[i+1]

print(dp[1])