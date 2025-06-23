import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

before = []
after = []

for _ in range(N):
    temp = list(map(int, input().strip().split()))
    before.append(temp)

for _ in range(N):
    temp = list(map(int, input().strip().split()))
    after.append(temp)
    
def is_same(arr1, arr2):
    for r in range(N):
        for c in range(M):
            if arr1[r][c] != arr2[r][c]:
                return False
    return True

if is_same(before, after):
    # 우연히 항체 값이 같은 경우
    print('YES')
    exit()

visited = [[False]*M for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(r, c, temp, original, vaccine):
    visited[r][c] = True
    temp[r][c]= vaccine
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            if not visited[nr][nc] and temp[nr][nc] == original: # 전파 가능
                dfs(nr, nc, temp, original, vaccine)

for r in range(N):
    for c in range(M):
        if before[r][c] != after[r][c] and not visited[r][c]: # 백신 투약 가능
            temp = [b[:] for b in before]
            original, vaccine = before[r][c], after[r][c]
            dfs(r, c, temp, original, vaccine)
            if is_same(temp, after):
                print('YES')
            else:
                print('NO')
            exit()