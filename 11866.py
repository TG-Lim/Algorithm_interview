# Silver 5
from collections import deque
N, K = map(int, input().split())
array = [i for i in range(1, N+1)]
queue = deque(array)
yoseputh = []
while queue:
    queue.rotate(-(K-1))
    v = queue.popleft()
    yoseputh.append(str(v))

yoseputh[0] = '<'+yoseputh[0]
yoseputh[-1] = yoseputh[-1]+'>'
print(', '.join(yoseputh))