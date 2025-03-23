import sys
input = sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().strip().split())
array = set() # 중복 입력 방지용

for _ in range(n):
    array.add(int(input()))

array = list(array)

dp = [INF]*(k+1)

# 배수들 채워넣기
for a in array:
    for i in range(a, k+1, a):
        if i % a == 0:
            dp[i] = min(dp[i], i//a)

# 서로 더해서 만들 수 있는 경우
for i in range(1, k+1):
    for a in array:
        if i+a <= k:
            dp[i+a] = min(dp[i+a], dp[i]+1)

if dp[k] == INF:
    print(-1)
else:
    print(dp[k])