# Silver 2
# BFS
import sys
from collections import deque

input = sys.stdin.readline
A, B = map(int, input().strip().split())

visited = set([A])
queue = deque([(A, 1)])

while queue:
    number, cnt = queue.popleft()
    next_number1 = number*2
    next_number2 = int(str(number)+'1')

    if next_number1 == B or next_number2 == B:
        print(cnt + 1)
        exit()

    if next_number1 < B and next_number1 not in visited:
        queue.append((next_number1, cnt+1))
        visited.add(next_number1)

    if next_number2 < B and next_number2 not in visited:
        queue.append((next_number2, cnt+1))
        visited.add(next_number2)

print(-1)