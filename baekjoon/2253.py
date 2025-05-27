from collections import deque
import sys
input = sys.stdin.readline
def solution():
    N, M = map(int, input().split())
    small = set(int(input()) for _ in range(M))

    dp = [set() for _ in range(N+1)]
    dp[1].add(0)
    queue = deque([(1, 0, 0)])  # (현재 위치, 마지막 점프, 총 점프 수)

    while queue:
        pos, last, cnt = queue.popleft()

        for jump in (last-1, last, last+1):
            if jump <= 0:
                continue
            nxt = pos + jump
            if nxt > N or nxt in small:
                continue
            if jump not in dp[nxt]:
                if nxt == N:
                    print(cnt + 1)  # 처음 도달 -> 최소 점프 수
                    return
                dp[nxt].add(jump)
                queue.append((nxt, jump, cnt + 1))

    print(-1)  # 도달 불가

solution()
