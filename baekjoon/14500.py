# Gold 4
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
array = []
for _ in range(N):
    array.append(list(map(int, input().strip().split())))

answer = 0

three_hor = [(-1, 0), (-1, 1), (-1, 2), (0, 3), (1, 2), (1, 1), (1, 0), (0, -1)]
three_ver = [(-1, 0), (0, 1), (1, 1), (2, 1), (3, 0), (2, -1), (1, -1), (0, -1)]

# 세 개 가로 한줄
for i in range(N):
    for j in range(M-2):
        temp = sum(array[i][j:j+3])
        for delta in three_hor:
            ni, nj = i + delta[0], j + delta[1]
            condition = (0 <= ni < N) and (0 <= nj < M)
            if condition:
                temp2 = temp + array[ni][nj]
                answer = max(answer, temp2)
# 세 개 세로 한줄
for i in range(N-2):
    for j in range(M):
        temp = sum([array[k][j] for k in range(i,i+3)])
        for delta in three_ver:
            ni, nj = i + delta[0], j + delta[1]
            condition = (0 <= ni < N) and (0 <= nj < M)
            if condition:
                temp2 = temp + array[ni][nj]
                answer = max(answer, temp2)

two_hor = [[(-1, 0), (1, 1)], [(1, 0), (-1, 1)]]
two_ver = [[(0, 1), (1, -1)], [(0, -1), (1, 1)]]

# 두 개 가로 한줄
for i in range(N):
    for j in range(M-1):
        temp = sum(array[i][j:j+2])
        for delta_list in two_hor:
            ni1, nj1 = i + delta_list[0][0], j + delta_list[0][1]
            ni2, nj2 = i + delta_list[1][0], j + delta_list[1][1]
            condition = (0<= ni1 < N) and (0 <= nj1 < M) and (0 <= ni2 < N) and (0 <= nj2 < M)
            if condition:
                temp2 = temp + array[ni1][nj1] + array[ni2][nj2]
                answer = max(answer, temp2)

# 두 개 세로 한줄
for i in range(N-1):
    for j in range(M):
        temp = sum([array[k][j] for k in range(i,i+2)])
        for delta_list in two_ver:
            ni1, nj1 = i + delta_list[0][0], j + delta_list[0][1]
            ni2, nj2 = i + delta_list[1][0], j + delta_list[1][1]
            condition = (0 <= ni1 < N) and (0 <= nj1 < M) and (0 <= ni2 < N) and (0 <= nj2 < M)
            if condition:
                temp2 = temp + array[ni1][nj1] + array[ni2][nj2]
                answer = max(answer, temp2)
                
# ㅁ 자
for i in range(N-1):
    for j in range(M-1):
        temp = sum([array[i][j], array[i][j+1], array[i+1][j], array[i+1][j+1]])
        answer = max(answer, temp)
                
print(answer)