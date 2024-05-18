# Silver 3
# 백트래킹

N, M = map(int, input().strip().split())
result = []
def backtracking(length):
    if length == M+1:
        print(' '.join(map(str, result)))
        return

    for i in range(1, N+1):
        result.append(i)
        backtracking(length+1)
        result.pop()

backtracking(1)