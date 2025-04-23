import sys
input = sys.stdin.readline

S = input().strip()
R, C = map(int, input().strip().split())
array = [list(input().strip()) for _ in range(R)]

dr = [-1, -1, -1,  0, 0, 1,  1,  1]
dc = [-1,  0,  1, -1, 1,-1,  0,  1]


length = len(S)

for r in range(R):
    for c in range(C):
        for i in range(8): # 8 방향
            positions = [(r+d*dr[i], c + d*dc[i]) for d in range(length)]
            if all(0 <= nr < R and 0 <= nc < C for nr, nc in positions): # 모든 성분이 범위 만족
                words = [array[pos[0]][pos[1]] for pos in positions]
                if ''.join(words) == S:
                    print(1)
                    exit()

print(0)