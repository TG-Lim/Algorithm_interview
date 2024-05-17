# Silver 4
# 1<= N <= 5000 -> O(N^2)
from collections import deque
N, K = map(int, input().strip().split())
array = [i for i in range(1, N+1)]
queue = deque(array)
result = []
for _ in range(N-1):
    for _ in range(K-1):
        q = queue.popleft()
        queue.append(q)
    q = queue.popleft()
    result.append(str(q))
q = queue.popleft()
result.append(str(q))
result[0] = '<'+result[0]
result[N-1] = result[N-1] + '>'
print(', '.join(result))