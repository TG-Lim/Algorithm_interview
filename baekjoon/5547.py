import sys
from collections import deque
input = sys.stdin.readline

W, H = map(int, input().split())
# 1. 패딩 추가된 그리드 생성 (0~H+1, 0~W+1)
grid = [[0]*(W+2) for _ in range(H+2)]
for i in range(1, H+1):
    row = list(map(int, input().split()))
    for j in range(1, W+1):
        grid[i][j] = row[j-1]

# 방문 기록
visited = [[False]*(W+2) for _ in range(H+2)]

# 6방향 델타: dh은 공통, dw는 홀짝 행별로 다름
dh = [-1, -1, 0, 0, 1, 1]
dw_odd  = [ 0,  1, -1,  1, 0,  1]  # 홀수는 왼쪽 아래로 내려감
dw_even = [-1,  0, -1,  1, -1, 0]  # 짝수는 오른쪽 아래로 내려감

ans = 0
q = deque()
# 2. (0,0)에서 시작
q.append((0,0))
visited[0][0] = True

while q:
    y, x = q.popleft()
    # 3. 현재 행 홀짝에 맞춰 델타 선택
    dw = dw_odd if (y % 2 == 1) else dw_even

    for d in range(6):
        ny, nx = y + dh[d], x + dw[d]
        # 격자 안에 있으면
        if 0 <= ny < H+2 and 0 <= nx < W+2:
            if grid[ny][nx] == 1:
                # 바깥 영역에서 건물을 만나면 벽 1개
                ans += 1
            elif not visited[ny][nx]:
                # 빈 칸(0)이면 계속 밖 영역 확장
                visited[ny][nx] = True
                q.append((ny, nx))

print(ans)