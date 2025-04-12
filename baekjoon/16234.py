import sys
input = sys.stdin.readline

N, L, R = map(int, input().strip().split())
array = [[0]*N for _ in range(N)]

for i in range(N):
    temp = list(map(int, input().strip().split()))
    for j in range(N):
        array[i][j] = temp[j]

if N == 1: # 1이면 아예 이동이 발생 못함
    print(0)
    exit()

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
answer = 0

def dfs(r, c, visited, map, group):
    if not visited[r][c]:
        visited[r][c] = True
        map[r][c] = group
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc] and L <= abs(array[r][c] - array[nr][nc]) <= R:
                    dfs(nr, nc, visited, map, group)
        return True
    return False

while True:
    cnt = 0
    map = [[-1]*N for _ in range(N)] # 어느 연합에 속하는 가
    visited = [[False]*N for _ in range(N)] # DFS 방문 관련 변수
    ## 지도 만들기
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                cnt += 1
                dfs(r=i, c=j, visited=visited, map=map, group=cnt)

    if cnt < N**2: # 연합 국가 존재 -> 인구 재할당. 이동 발생 안하면 N**2 나와야 함
        answer += 1
        temp = {}
        for i in range(N):
            for j in range(N):
                if map[i][j] not in temp:
                    temp[map[i][j]] = [array[i][j]]
                else:
                    temp[map[i][j]].append(array[i][j])

        people = {k: int(sum(v)/len(v)) for k, v in temp.items()}
        for i in range(N):
            for j in range(N):
                array[i][j] = people[map[i][j]]

    else:
        break

print(answer)