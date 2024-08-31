# Gold 4
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

array = [[]]
for _ in range(N):
    temp = [0]*(N+1)
    array.append(temp)

K = int(input())

if K > 0:
    for _ in range(K):
        r, c = map(int, input().split())
        array[r][c] = 1 # 사과 있음

L = int(input())

change_timing = {}
for _ in range(L):
    t, direction = input().split()
    change_timing[t] = direction

dr = [-1, 1, 0, 0] # 상, 하, 좌, 우
dc = [0, 0, -1, 1] # 상, 하, 좌, 우

def change_direction(d: int, direction: str):
    change_d = None
    if d == 0 and direction == 'L': # 좌
        change_d = 2
    if d == 0 and direction == 'D': # 우
        change_d = 3
    if d == 1 and direction == 'L': # 우
        change_d = 3
    if d == 1 and direction == 'D': # 좌
        change_d = 2
    if d == 2 and direction == 'L': # 하
        change_d = 1
    if d == 2 and  direction == 'D': # 상
        change_d = 0
    if d == 3 and direction == 'L': # 상
        change_d = 0
    if d == 3 and direction == 'D': # 하
        change_d = 1

    return change_d

isbody = [[False]*(N+1) for _ in range(N+1)] # 현재 칸이 몸의 여부인지를 확인하는 변수
isbody[1][1] = True

snakes = deque([(1, 1, 3)]) # r, c, 보는 방향, 시간
# 처음 인덱스: 꼬리
# 마지막 인덱스: 머리
# 처음에는 꼬리와 머리의 위치가 같음
# 뱀 게임은 먼저 들어간 칸이 먼저 나감

t = 0
while True:
    t += 1
    r, c, d = snakes[-1] # 머리 늘림 (pop 연산 X)
    nr, nc = r + dr[d], c + dc[d]

    if nr > N or nr < 1 or nc > N or nc < 1 or isbody[nr][nc]: # 벽에 부딪치거나 자기 몸임
        print(t)
        exit()
    
    # 머리 이동
    isbody[nr][nc] = True

    if array[nr][nc] == 1: # 다음 칸이 사과인 경우
        array[nr][nc] = 0 # 사과 먹고 나머지는 그대로
    
    else: # 사과가 아닌 경우 -> 꼬리가 움직이므로 데크에서 꼬리 삭제
        tail_r, tail_c, _ = snakes.popleft()
        isbody[tail_r][tail_c] = False
    
    if str(t) in change_timing: # 방향 바꿔야 하는 시기
        direction = change_timing[str(t)]
        new_d = change_direction(d, direction)
        snakes.append((nr, nc, new_d))
    else:
        snakes.append((nr, nc, d))