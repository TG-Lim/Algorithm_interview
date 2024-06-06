# Silver 3
# Backtracking

N, M = map(int, input().strip().split())
array = [i for i in range(1, N+1)]

result = []
def backtracking(temp, n):
    if n == M:
        result.append(' '.join(str(t) for t in temp))
        return
    
    for a in array:
        if temp[-1] <= a: # 같거나 큰 값이 array 로 부터 추가 됨
            temp2 = temp[:]
            temp2.append(a)
            backtracking(temp2, n+1)
    
for a in array:
    backtracking([a], 1)
for r in result:
    print(r)