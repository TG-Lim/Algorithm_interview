import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

def dfs(x, prefer, visited, finished):
    if finished[x]:
        return 0
    if visited[x]:
        cycle_size = 1
        curr = prefer[x]
        while curr != x:
            cycle_size += 1
            curr = prefer[curr]
        return cycle_size

    visited[x] = True
    cycle_size = dfs(prefer[x], prefer, visited, finished)
    finished[x] = True
    
    return cycle_size

T = int(input())
answers = []
for _ in range(T):
    n = int(input())
    prefer = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    finished = [False] * (n + 1)
    team_count = 0

    for i in range(1, n + 1):
        if not finished[i]:
            team_count += dfs(i, prefer, visited, finished)

    answers.append(n - team_count)

print('\n'.join(map(str, answers)))