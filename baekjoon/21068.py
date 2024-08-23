# Gold 5
import sys
input = sys.stdin.readline

N = int(input())
array = [[0]*(N) for _ in range(N)]

likes = {}

for _ in range(N**2):
    temp = list(map(int, input().split()))
    likes[str(temp[0])] = (temp[1:])

seated = [[False]*(N) for _ in range(N)]
        
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

for n in likes.keys():
    cnt = 0
    positions = []
    for r in range(N):
        for c in range(N):
            temp = 0
            if not seated[r][c]: # 빈 칸인 경우
                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    if 0 <= nr < N and 0 <= nc < N and array[nr][nc] in likes[n]: # 범위 내에 있고, 좋아하는 학생이 인접한 경우
                        temp += 1
            
                if temp > cnt: # 현재 값 보다 인접한 곳에 좋아하는 학생이 많음
                    cnt = temp
                    positions = [(r, c)] # 길이가 1인 리스트로 변경
                if temp == cnt: # 현재 값 보다 인접한 곳에 좋아하는 학생이 같음
                    positions.append((r, c)) # 성분 추가

    if len(positions) == 1: # 좋아하는 학생들이 많이 앉아 있는 자리가 1개
        array[positions[0][0]][positions[0][1]] = int(n)
        seated[positions[0][0]][positions[0][1]] = True
    
    else: # 좋아하는 학생들이 많이 앉아 있는 자리가 여러개
        cnt2 = 0
        positions2 = []
        for r, c in positions:
            temp2 = 0
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < N and 0<= nc < N and array[nr][nc] == 0:
                    temp2 += 1
            
            if temp2 > cnt2:
                cnt2 = temp2
                positions2 = [(r, c)]
            
            if temp2 == cnt2:
                positions2.append((r, c))

        if len(positions2) == 1:
            array[positions2[0][0]][positions2[0][1]] = int(n)
            seated[positions2[0][0]][positions2[0][1]] = True
        else:
            sorted_list = sorted(positions2, key=lambda x: (x[0], x[1]))
            array[sorted_list[0][0]][sorted_list[0][1]] = int(n)
            seated[sorted_list[0][0]][sorted_list[0][1]] = True

total_like = 0
for r in range(N):
    for c in range(N):
        temp = 0
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and array[nr][nc] in likes[str(array[r][c])]: # 인접한 자리에 좋아하는 사람 앉음
                temp += 1
        
        if temp > 0:
            total_like += 10**(temp-1)

print(total_like)