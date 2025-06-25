import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline
N = int(input())
tteoks = []
for _ in range(N):
    temp = list(map(int, input().strip().split()))
    tteoks.append(temp[1:])
    
if N == 1: # 무조건 가능
    print(tteoks[0][0])
    exit()

visited = [[False]*10 for _ in range(N+1)]
# visited[i][n]: i번째 날에 n 번째 떡을 준 경우

result = []

def backtracking(i: int, prev: int):
    if i == N:
        return True
    
    if visited[i][prev]:
        return False
    
    visited[i][prev] = True
    
    for tteok in tteoks[i]:
        if tteok != prev:
            result.append(tteok)
            if backtracking(i+1, tteok):
                return True
            result.pop()
    
    return False

result = []
if backtracking(0, 0):
    for r in result:
        print(r)
else:
    print(-1)