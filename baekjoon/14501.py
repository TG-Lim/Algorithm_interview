# Silver 3
N = int(input())
T = []
P = []
for _ in range(N):
    t, p = map(int, input().strip().split())
    T.append(t)
    P.append(p)

best = 0

def backtracking(cost, day):
    global best
    if day >= N:
        best = max(best, cost)
        return
    
    if day + T[day] <= N:
        backtracking(cost + P[day], day + T[day])
    
    backtracking(cost, day + 1)

backtracking(0, 0)
print(best)