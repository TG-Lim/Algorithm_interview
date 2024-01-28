import sys
chess=[['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
n, m = map(int, sys.stdin.readline().split())
result = 64
chess_array = []
for _ in range(n):
    chess_array.append(list(sys.stdin.readline().strip('\n')))
def check(x, y):
    cnt=0
    for i in range(8):
        for j in range(8):
            if chess[i][j]==chess_array[x+i][y+j]:
                cnt+=1
    # 체스판 2가지 경우중 더 맞은 거 찾기
    return min(cnt, 64-cnt)
for i in range(n-7):
    for j in range(m-7):
        result=min(result, check(i, j))
print(result)