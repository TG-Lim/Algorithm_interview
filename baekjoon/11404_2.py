import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
inf = int(1e9)
array = [[inf]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    array[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().strip().split())
    array[a][b] = min(array[a][b], c)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            array[a][b] = min(array[a][b], array[a][k]+array[k][b])

for i in range(1, n+1):
    temp = [0 if a == inf else a for a in array[i][1:]]
    print(' '.join(str(t) for t in temp))