# Gold 5
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
array = [[]]
for _ in range(N):
    temp = [0] # 인덱스 숫자 맞추기용
    temp.extend(list(map(int, input().split())))

    array.append(temp)

moves = []
for _ in range(M):
    moves.append(list(map(int, input().split()))) # d, s 순서

dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]

def move_cloud(r, c, d, s):
    nr = r + dr[d]*s
    nc = c + dc[d]*s

    if nr > N:
        nr = (nr % N)
        if nr == 0:
            nr = N
    
    if nr < 1:
        nr = N - ((-nr)%N)
    
    if nc > N:
        nc = (nc % N)
        if nc == 0:
            nc = N
    
    if nc < 1:
        nc = N - ((-nc)%N)
    
    return nr, nc

def answer():
    total = 0
    for r in range(1, N+1):
        for c in range(1, N+1):
            total += array[r][c]
    
    print(total)

magic_dr = [-1, -1, 1, 1]
magic_dc = [1, -1, 1, -1]

clouds = deque([(N, 1), (N, 2), (N-1, 1), (N-1, 2)])

for m in range(M):
    removes = set()
    d, s = moves[m][0], moves[m][1]
    for _ in range(len(clouds)):
        r, c = clouds.popleft()
        nr, nc = move_cloud(r, c, d, s) # 구름 이동
        array[nr][nc] += 1 # 비내림
        removes.add((nr, nc)) # 비내리고 사라짐
    
    for remove_cloud in removes:
        nr, nc = remove_cloud[0], remove_cloud[1]
        for i in range(4):
            nnr, nnc = nr + magic_dr[i], nc + magic_dc[i]
            if 1<= nnr <= N and 1 <= nnc <= N and array[nnr][nnc] > 0: # 칸의 범위 안이고, 물이 있음
                array[nr][nc] += 1 # 물복사버그
    
    for r in range(1, N+1):
        for c in range(1, N+1):
            if (r, c) not in removes and array[r][c] >= 2:
                clouds.append((r, c))
                array[r][c] -= 2

answer()