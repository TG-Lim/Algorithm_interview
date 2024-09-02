# Gold 5
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
answers = []

for _ in range(t):
    n = int(input())
    positions = []
    for _ in range(n+2):
        temp_x, temp_y = map(int, input().split())
        positions.append((temp_x, temp_y))

    array = [[0]*(n+2) for _ in range(n+2)]
    for i in range(n+2):
        for j in range(n+2):
            if i != j:
                distance = abs(positions[i][0]-positions[j][0])+abs(positions[i][1]-positions[j][1])
                array[i][j] = distance
                array[j][i] = distance
    
    visited = [False]*(n+2)
    queue = deque([0])
    visited[0] = True
    while queue:
        node = queue.popleft()
        for j in range(n+2):
            if array[node][j] <= 1000 and not visited[j]:
                queue.append(j)
                visited[j] = True
    
    if visited[-1]:
        answers.append("happy")
    else:
        answers.append("sad")

for a in answers:
    print(a)