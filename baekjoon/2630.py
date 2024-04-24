# Silver 2
import sys
N = int(input())
array = []
for i in range(N):
    array.append(list(map(int, sys.stdin.readline().strip().split())))
result = []
def check(x, y, N):
    color = array[x][y]
    for i in range(x, x+N):
        for j in range(y,y+N):
            if color != array[i][j]: # 색깔 다르면
                check(x, y, N//2)
                check(x, y+N//2, N//2)
                check(x+N//2, y, N//2)
                check(x+N//2, y+N//2, N//2)
                return None
    if color == 0:
        result.append(0)
    else:
        result.append(1)

check(0,0,N)
print(result.count(0))
print(result.count(1))