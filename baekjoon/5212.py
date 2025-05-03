R, C = map(int, input().strip().split())
array = [list(input().strip()) for _ in range(R)]

lands = []
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

for r in range(R):
    for c in range(C):
        if array[r][c] == 'X':
            lands.append((r, c))

gone = []
for r, c in lands:
    cnt = 0
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < R and 0 <= nc < C: # 지도 범위 내
            if array[nr][nc] == '.': # 바다
                cnt += 1
        else: # 지도 범위 밖은 바다
            cnt += 1

    if cnt >= 3:
        gone.append(True)
    else:
        gone.append(False)

for i in range(len(gone)):
    if gone[i]:
        r, c = lands[i]
        array[r][c] = '.'

land_r = []
land_c = []
for r in range(R):
    for c in range(C):
        if array[r][c] == 'X':
            land_r.append(r)
            land_c.append(c)

land_r.sort()
land_c.sort()

r_min, r_max = land_r[0], land_r[-1]
c_min, c_max = land_c[0], land_c[-1]

for r in range(r_min, r_max+1):
    temp = array[r][c_min:c_max+1]
    print(''.join(temp))