N = int(input())
array = list(map(int, input().strip().split()))

dp = array[:] # dp[i]: 인덱스 i에서 끝났을 때 합의 최대값

for i in range(N):
    for j in range(i):
        if array[j] < array[i]: # 값이 작으면
            dp[i] = max(dp[i], dp[j] + array[i])

print(max(dp))