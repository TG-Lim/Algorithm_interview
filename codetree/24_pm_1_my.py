import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 0, 1, 0] # 북 동 남 서
dc = [0, 1, 0, -1]

def check_in_forest(r, c):
    return (1 <= r <= R) and (1 <= c <= C)

def can_move(r, dr, c, dc):
    if dr == 1 and dc == 0:  # 남쪽
        return (r+2 <= R and c+1 <= C and c-1 >= 1 and
                all(array[r+i][c+j] == 0 for i, j in [(1, -1), (2, 0), (1, 1)]))
    elif dr == 1 and dc == -1:  # 남서쪽
        return (r+2 <= R and c-2 >= 1 and
                all(array[r+i][c+j] == 0 for i, j in [(-1, -1), (0, -2), (1, -2), (1, -1), (2, -1)]))
    elif dr == 1 and dc == 1:  # 남동쪽
        return (r+2 <= R and c+2 <= C and
                all(array[r+i][c+j] == 0 for i, j in [(-1, 1), (0, 2), (1, 2), (1, 1), (2, 1)]))
    return False


def get_movable_direction(r, c, preferred_direction):
    directions = [(1, 0), (1, -1), (1, 1)]
    for dr, dc in directions:
        if preferred_direction == (dr, dc):
            if can_move(r, dr, c, dc):
                return dr, dc

    for dr, dc in directions:
        if can_move(r, dr, c, dc):
            return dr, dc

    return 0, 0  # 이동 불가능

def check_golem_out(array):
    for j in range(1, C+1):
        if array[0][j] == 1: # 골렘이 밖에 튀어나와 있음
            return True
    return False



def stack_golem(c, d, array):
    start_r = 0
    start_c = c
    exit_d = d
    preferred_direction = (1, 0)  # 초기에는 남쪽 방향 선호

    while True:
        delta_r, delta_c = get_movable_direction(start_r, start_c, preferred_direction)
        if delta_r == 0 and delta_c == 0:
            break

        start_r += delta_r
        start_c += delta_c

        if delta_r == 1 and delta_c == -1:  # 서쪽으로 회전하면서 이동
            exit_d = (exit_d - 1) % 4
            preferred_direction = (1, -1)
        elif delta_r == 1 and delta_c == 1:  # 동쪽으로 회전하면서 이동
            exit_d = (exit_d + 1) % 4
            preferred_direction = (1, 1)
        else:
            preferred_direction = (1, 0)

    array[start_r][start_c] = 'c' # 중심
    exit_r, exit_c = start_r + dr[exit_d], start_c + dc[exit_d]
    array[exit_r][exit_c] = 'e' # 탈출구
    for d in range(4):
        nr, nc = start_r + dr[d], start_c + dc[d]
        if array[nr][nc] == 0:
            array[nr][nc] = 1 # 골렘 쌓음

    return start_r, start_c

def get_nearest_center(r, c):
    dist = 141  # 큰 초기값
    near_r, near_c = None, None
    for i in range(1, R+1):
        for j in range(1, C+1):
            if array[i][j] == 'c':
                temp = abs(i - r) + abs(j - c)
                if temp < dist:
                    dist = temp
                    near_r, near_c = i, j
    print(f"Nearest center to ({r}, {c}) is ({near_r}, {near_c})")
    return near_r, near_c

def bfs(center_r, center_c):
    visited = [[False]*(C+1) for _ in range(R+1)]
    queue = deque([(center_r, center_c)])
    visited[center_r][center_c] = True

    southest = center_r

    while queue:
        r, c = queue.popleft()
        southest = max(southest, r)

        for d in range(4):  # 남, 동, 북, 서 순서로 탐색
            nr, nc = r + dr[d], c + dc[d]
            if check_in_forest(nr, nc):
                if array[r][c] == 'e' and array[nr][nc] != 0:
                    # 현재가 탈출구 이고 다음 칸이 골렘의 일부인 경우
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))

                        near_r, near_c = get_nearest_center(nr, nc)
                        if not visited[near_r][near_c]:
                            visited[near_r][near_c] = True
                            queue.append((near_r, near_c))

                elif array[r][c] == 'c' and array[nr][nc] != 0:
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        array.append((nr, nc))

    return southest

if __name__ == "__main__":
    R, C, K = map(int, input().split())
    golems = []
    for _ in range(K):
        c, d = map(int, input().split())
        golems.append((c, d))

    array = [[0]*(C+1) for _ in range(R+1)]
    answer = 0
    cnt = 0
    for c, d in golems:
        center_r, center_c = stack_golem(c, d, array)
        if check_golem_out(array):
            array = [[0]*(C+1) for _ in range(R+1)] # 배열 초기화
        else:
            answer += bfs(center_r, center_c)

    print(answer)