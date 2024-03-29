# Silver 4
from collections import deque
n = int(input())
cards = [i for i in range(1,n+1)]
queue = deque(cards)

while len(queue) > 1:
    p = queue.popleft()
    q = queue.popleft()
    queue.append(q)

print(queue[0])