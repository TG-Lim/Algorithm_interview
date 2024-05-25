# Gold 5
# Brute Force
import sys
from itertools import combinations

input = sys.stdin.readline
N = int(input())

array = []
for _ in range(N):
    array.append(list(input().strip().split()))

positions = []
teachers = []
for i in range(N):
    for j in range(N):
        if array[i][j] == 'X':
            positions.append((i, j))
        if array[i][j] == 'T':
            teachers.append((i, j))

num_teacher = len(teachers)

def check_student(x, y): # 학생 발견하면 True, 아니면 False
    if x < N-1: # 동쪽 체크
        for i in range(x+1, N):
            if array[i][y] == 'O':
                break
            if array[i][y] == 'S':
                return True

    if x > 0: # 서쪽 체크
        for i in range(1, x+1):
            if array[x-i][y] == 'O':
                break
            if array[x-i][y] == 'S':
                return True

    if y > 0: # 북쪽 체크
        for j in range(1, y+1):
            if array[x][y-j] == 'O':
                break
            if array[x][y-j] == 'S':
                return True
    if y < N-1: # 남쪽 체크
        for j in range(y+1, N):
            if array[x][j] == 'O':
                break
            if array[x][j] == 'S':
                return True
    return False

obstacle_list = list(combinations(positions, 3))
# # ((0, 0), (0, 2), (0, 3))
for obstacle in obstacle_list:
    cnt = 0
    for i in range(3):
        array[obstacle[i][0]][obstacle[i][1]] = 'O'

    for teacher in teachers:
        if not check_student(teacher[0], teacher[1]): # 학생 발견
            cnt += 1
    if cnt == num_teacher:
        print("YES")
        exit()

    for i in range(3): # 다시 원상복구
        array[obstacle[i][0]][obstacle[i][1]] = 'X'

print("NO")