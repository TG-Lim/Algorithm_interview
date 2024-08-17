# 1 <= N, M <= 20
# 1 <= K <= 1000

import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().strip().split())

array = []

for _ in range(N):
    temp = list(map(int, input().split()))
    array.append(temp)

directions = list(map(int, input().split()))

dice = {f'{i}': 0 for i in range(1, 7)} # 주사위 써진 거 초기화

positions = {
    "top" : 1,
    "bottom" : 6,
    "left" : 4,
    "right" : 3,
    "front" : 5,
    "back" : 2
}

def change_direction(direction: int):
    if direction == 1: # 동쪽
        pre_top = positions['top']
        pre_left = positions['left']
        pre_right = positions['right']
        pre_bottom = positions['bottom']

        positions['top'], positions['bottom'], positions['left'], positions['right'] = pre_left, pre_right, pre_bottom, pre_top
    
    if direction == 2: # 서쪽
        pre_top = positions['top']
        pre_left = positions['left']
        pre_right = positions['right']
        pre_bottom = positions['bottom']

        positions['top'], positions['bottom'], positions['left'], positions['right'] = pre_right, pre_left, pre_top, pre_bottom
    
    if direction == 3: # 북쪽
        pre_top = positions['top']
        pre_bottom = positions['bottom']
        pre_front = positions['front']
        pre_back = positions['back']

        positions['top'], positions['bottom'], positions['front'], positions['back'] = pre_front, pre_back, pre_bottom, pre_top

    if direction == 4: # 남쪽
        pre_top = positions['top']
        pre_bottom = positions['bottom']
        pre_front = positions['front']
        pre_back = positions['back']

        positions['top'], positions['bottom'], positions['front'], positions['back'] = pre_back, pre_front, pre_top, pre_bottom

now_x, now_y = x, y
dx = [0, 0, 0, -1, 1] # 인덱스 맞추기용, 동, 서, 북, 남
dy = [0, 1, -1, 0, 0]

for direction in directions:
    nx, ny = now_x + dx[direction], now_y + dy[direction]
    if (0 <= nx < N) and (0 <= ny < M): # 지도 범위 내
        now_x, now_y = nx, ny # 위치 업데이트
        change_direction(direction) # 주사위 업데이트
        if array[now_x][now_y] != 0: # 현재 지도에서 칸이 0이 아닌 경우 -> 주사위로 복사 시키고 칸은 0
            dice[str(positions['bottom'])] = array[now_x][now_y]
            array[now_x][now_y] = 0
        
        else: # 현재 지도에서 칸이 0인 경우 -> 주사위의 밑칸이 지도로 복사 됨
            array[now_x][now_y] = dice[str(positions['bottom'])]
        
        print(dice[str(positions['top'])])
    
    else:
        continue