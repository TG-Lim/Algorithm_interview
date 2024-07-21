from collections import deque

N, M, K = map(int, input().strip().split())

A = [[0] * (N+1)] + [[0] + list(map(int, input().strip().split())) for _ in range(N)]

earth = [[5]*(N+1) for _ in range(N+1)] # 비료 상태
trees = [[deque() for _ in range(N+1)] for _ in range(N+1)] # 나무
dead = [[list() for _ in range(N+1)] for _ in range(N+1)] # 죽은 나무 저장

for _ in range(M):
    x, y, z = map(int, input().strip().split())
    trees[x][y].append(z)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def spring_summer():
    for i in range(1, N+1):
        for j in range(1, N+1):
            cnt = len(trees[i][j]) # 현재 위치에 있는 나무 개수
            for k in range(cnt):
                if earth[i][j] < trees[i][j][k]: # 나무 죽는 경우
                    for _ in range(k, cnt):
                        dead[i][j].append(trees[i][j].pop())
                    break
                else: # 나무 성장
                    earth[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
    
    # 죽은 나무 비료로
    for i in range(1, N+1):
        for j in range(1, N+1):
            while dead[i][j]:
                earth[i][j] += int((dead[i][j].pop())/2)

def fall_winter():
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(len(trees[i][j])):
                if trees[i][j][k] % 5 == 0: # 나무 번식
                    for d in range(8):
                        nx, ny = i + dx[d], j + dy[d]
                        if nx < 1 or nx > N or ny < 1 or ny > N: # 밭 범위 벗어나는 경우
                            continue
                        trees[nx][ny].appendleft(1)
            
            earth[i][j] += A[i][j]

for _ in range(K):
    spring_summer()
    fall_winter()

answer = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        answer += len(trees[i][j])

print(answer)