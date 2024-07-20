# Gold 3
# DP

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

answers = []

for _ in range(T):
    N, K = map(int, input().strip().split())
    times = list(map(int, input().strip().split()))
    before = [set() for _ in range(N)]
    after = [set() for _ in range(N)]
    in_degree = [0]*N

    for _ in range(K):
        a, b = map(int, input().strip().split())
        before[b-1].add(a-1)
        after[a-1].add(b-1)
        in_degree[b-1] += 1
    
    queue = deque([i for i in range(N) if in_degree[i] == 0])
    dp = [0]*N

    for i in queue:
        dp[i] = times[i]
    
    while queue:
        current = queue.popleft()
        for next_building in after[current]:
            in_degree[next_building] -= 1
            dp[next_building] = max(dp[next_building], dp[current] + times[next_building])
            if in_degree[next_building] == 0:
                queue.append(next_building)
    
    W = int(input())
    answers.append(dp[W-1])

for a in answers:
    print(a)