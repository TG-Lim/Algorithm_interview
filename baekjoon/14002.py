N = int(input())
array = list(map(int, input().strip().split()))

dp = [1]*N # dp[i]: array[i] 가 마지막 원소일 때 가긴부수 길이

parent = [None for _ in range(N)]

for i in range(N):
    for j in range(i):
        if array[j] < array[i] and dp[i] < dp[j] + 1:
            dp[i] = max(dp[i], dp[j]+1)
            parent[i] = j

print(max(dp))
max_index = dp.index(max(dp))
paths = [str(array[max_index])]
index = max_index

while parent[index] != None:
    index = parent[index]
    paths.append(str(array[index]))

print(' '.join(paths[::-1]))