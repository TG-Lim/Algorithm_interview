import sys
import heapq
input = sys.stdin.readline

N = int(input())
array = []
for _ in range(N):
    s, t = map(int, input().strip().split())
    array.append((s, t))
array.sort()


h = []

heapq.heappush(h, array[0][1])

for i in range(1, N):
    s, t = array[i]

    if h[0] <= s:
        heapq.heappop(h)
    
    heapq.heappush(h, t)

print(len(h))