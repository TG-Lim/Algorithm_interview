import sys
from collections import deque
input = sys.stdin.readline

dh = [-1, 1, 0, 0]
dw = [0, 0, 1, -1]

dh_horse = [-2, -2, -1, -1, 1, 1, 2, 2]
dw_horse = [1, -1, -2, 2, -2, 2, 1, -1]

if __name__ == '__main__':
    K = int(input())
    W, H = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(H)]

    visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
    queue = deque()
    queue.append((0, 0, 0, 0))  # h, w, moves, horse_moves_used
    visited[0][0][0] = 1  # Mark starting position as visited with 0 horse moves

    while queue:
        h, w, moves, k = queue.popleft()

        if h == H - 1 and w == W - 1:
            print(moves)
            exit()

        # Horse moves
        if k < K:
            for i in range(8):
                nh = h + dh_horse[i]
                nw = w + dw_horse[i]
                nk = k + 1
                if 0 <= nh < H and 0 <= nw < W and array[nh][nw] == 0 and not visited[nh][nw][nk]:
                    visited[nh][nw][nk] = 1
                    queue.append((nh, nw, moves + 1, nk))

        # Normal moves
        for i in range(4):
            nh = h + dh[i]
            nw = w + dw[i]
            if 0 <= nh < H and 0 <= nw < W and array[nh][nw] == 0 and not visited[nh][nw][k]:
                visited[nh][nw][k] = 1
                queue.append((nh, nw, moves + 1, k))

    print(-1)