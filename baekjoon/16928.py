# Gold 5
# BFS + 최적화 문제
from collections import deque
N, M = map(int, input().split())
ladder = {}
snake = {}
for _ in range(N):
    dep, arr = map(int, input().split())
    ladder[dep] = arr
for _ in range(M):
    dep, arr = map(int, input().split())
    snake[dep] = arr

counts = [float('inf')]*101
counts[1] = 0 # 시작점

queue = deque([1])

while queue:
    v = queue.popleft()
    for d in range(1, 7):
        arrival = v + d
        if arrival > 100:
            continue
        if arrival in ladder: # 사다리 인 경우 사다리로 최종 도착지 변경
            arrival = ladder[arrival]
        if arrival in snake: # 뱀인 경우 뱀으로 최종 도착지 변경
            arrival = snake[arrival]

        if counts[v] + 1 < counts[arrival]: # 기존 도착 횟수보다 더 우수한 경우 횟수 바꿈
            counts[arrival] = counts[v] + 1
            queue.append(arrival)

print(counts[100])