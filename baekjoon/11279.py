# Silver 2
import heapq
import sys
N = int(input())
heap = []
result = []
for _ in range(N):
    n = int(sys.stdin.readline().strip())
    if n == 0:
        if not heap: # 리스트가 비어 있는 경우
            result.append("0\n")
        else:
            big = heapq.heappop(heap)
            result.append(f"{big[1]}\n") # 최소값 출력
    else:
        heapq.heappush(heap, (-n,n))

sys.stdout.write(''.join(result))