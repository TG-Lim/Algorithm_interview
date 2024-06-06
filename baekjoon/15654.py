N, M = map(int, input().strip().split())
array = list(map(int, input().strip().split()))
array.sort()

result = []

def backtracking(temp, n):
    if n == M:
        result.append(temp[:])
        return
    
    for a in array:
        if a not in temp:
            temp.append(a)
            backtracking(temp, n+1)
            temp.pop()

backtracking([], 0)

for r in result:
    print(' '.join(str(r2) for r2 in r))