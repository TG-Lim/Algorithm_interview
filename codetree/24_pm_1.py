import sys

R, C, K = 0, 0, 0
score, rMax = 0, 0
m, gArr = [], []
di, dj = [-1, 0, 1, 0], [0, 1, 0, -1]
v = []

def main():
    global R, C, K, score, m, gArr, v

    R, C, K = map(int, sys.stdin.readline().split())
    score = 0
    init_map()
    gArr = [[] for _ in range(K)]

    for k in range(K):
        c, e = map(int, sys.stdin.readline().split())
        c -= 1  # 0-based indexing

        global rMax
        rMax = 0
        v = [False] * K
        drop(k, -2, c, e)

    print(score)

def drop(idx, ci, cj, e):
    global score, rMax

    while True:
        if ci == R - 2:
            break

        if ((ci == -2 and m[ci + 2][cj] == -1) or 
            (m[ci + 2][cj] == -1 and m[ci + 1][cj - 1] == -1 and m[ci + 1][cj + 1] == -1)):
            ci += 1
            continue

        if cj >= 2:
            if ((ci == -2 and m[ci + 2][cj - 1] == -1) or 
                ((ci == -1) and m[ci + 2][cj - 1] == -1 and m[ci + 1][cj - 1] == -1 and m[ci + 1][cj - 2] == -1) or 
                (m[ci + 2][cj - 1] == -1 and m[ci + 1][cj - 1] == -1 and m[ci + 1][cj - 2] == -1 and m[ci][cj - 2] == -1)):
                ci += 1
                cj -= 1
                e = (e + 3) % 4
                continue

        if cj < C - 2:
            if ((ci == -2 and m[ci + 2][cj + 1] == -1) or 
                ((ci == -1) and m[ci + 2][cj + 1] == -1 and m[ci + 1][cj + 1] == -1 and m[ci + 1][cj + 2] == -1) or 
                (m[ci + 2][cj + 1] == -1 and m[ci + 1][cj + 1] == -1 and m[ci + 1][cj + 2] == -1 and m[ci][cj + 2] == -1)):
                ci += 1
                cj += 1
                e = (e + 1) % 4
                continue

        break

    if ci <= 0:
        init_map()
        return

    m[ci][cj] = m[ci - 1][cj] = m[ci][cj + 1] = m[ci + 1][cj] = m[ci][cj - 1] = idx
    gArr[idx] = [ci, cj, e]
    move_golem(idx)
    score += rMax

def move_golem(idx):
    global rMax
    v[idx] = True
    ri = gArr[idx][0] + 2
    rMax = max(rMax, ri)

    e = gArr[idx][2]
    ri = gArr[idx][0] + di[e]
    rj = gArr[idx][1] + dj[e]

    for d in range(4):
        ni = ri + di[d]
        nj = rj + dj[d]
        if ni < 0 or ni >= R or nj < 0 or nj >= C:
            continue
        if m[ni][nj] == -1 or v[m[ni][nj]]:
            continue
        move_golem(m[ni][nj])

def init_map():
    global m
    m = [[-1] * C for _ in range(R)]

if __name__ == "__main__":
    main()