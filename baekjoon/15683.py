# Gold 3
import sys
sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline

N, M = map(int, input().strip().split())
array = []

for _ in range(N):
    array.append(list(map(int, input().strip().split())))

def count_unseen(array):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if array[i][j] == 0:
                cnt += 1

    return cnt

def deep_copy(arr):
    return [row[:] for row in arr]

cameras = []
for i in range(N):
    for j in range(M):
        if array[i][j] > 0 and array[i][j] < 6:
            cameras.append((i, j, array[i][j])) # x, y, 카메라 종류

def install_camera(array, x, y, direction):
    if direction == 0: # 동쪽으로
        for j in range(y, M):
            if array[x][j] == 6:
                break
            if array[x][j] == 0:
                array[x][j] = '#'
    
    if direction == 1: # 서쪽으로
        for j in range(y, -1, -1):
            if array[x][j] == 6:
                break
            if array[x][j] == 0:
                array[x][j] = '#'

    if direction == 2: # 북쪽으로
        for i in range(x, -1, -1):
            if array[i][y] == 6:
                break
            if array[i][y] == 0:
                array[i][y] = '#'

    if direction == 3: # 남쪽으로
        for i in range(x, N):
            if array[i][y] == 6:
                break
            if array[i][y] == 0:
                array[i][y] = '#'

def backtracking(array, num):
    if num == len(cameras):
        unseen = count_unseen(array)
        return unseen
    else:
        x, y, camera_type = cameras[num]
        min_unseen = 65 # 8 X 8 이 최대

        if camera_type == 1:
            for direction in range(4):
                new_array = deep_copy(array)
                install_camera(new_array, x, y, direction)
                min_unseen = min(min_unseen, backtracking(new_array, num+1))
        
        if camera_type == 2:
            for directions in [(0, 1), (2, 3)]:
                new_array = deep_copy(array)
                for direction in directions:
                    install_camera(new_array, x, y, direction)
                min_unseen = min(min_unseen, backtracking(new_array, num+1))
        
        if camera_type == 3:
            for directions in [(0, 2), (0, 3), (1, 2), (1, 3)]:
                new_array = deep_copy(array)
                for direction in directions:
                    install_camera(new_array, x, y, direction)
                min_unseen = min(min_unseen, backtracking(new_array, num+1))

        if camera_type == 4:
            for directions in [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]:
                new_array = deep_copy(array)
                for direction in directions:
                    install_camera(new_array, x, y, direction)
                min_unseen = min(min_unseen, backtracking(new_array, num+1))

        if camera_type == 5:
            new_array = deep_copy(array)
            for direction in range(4):
                install_camera(new_array, x, y, direction)
            min_unseen = min(min_unseen, backtracking(new_array, num+1))

        return min_unseen
    
result = backtracking(array, 0)
print(result)