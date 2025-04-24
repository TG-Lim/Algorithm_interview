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

answer = -1

for s, t in array:
    if not h:
        heapq.heappush(h, t)
        answer = 1
        continue

    if h[0] <= s: # h[0]: 강의 종료시간 중 가장 빨리 끝나는 시간. 수업 더 놓을 수 있음
        h.pop(0)
        heapq.heappush(h, t)
    else:
        heapq.heappush(h, t)
    
    answer = max(answer, len(h))

print(answer)