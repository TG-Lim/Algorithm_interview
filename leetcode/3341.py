from typing import List
from collections import deque
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])

        dr = [-1, 1, 0, 0]
        dc = [0, 0, 1, -1]

        queue = deque([(0, 0, 0)]) # r, c, t
        visited = [[int(1e10)]*m for _ in range(n)]
        while queue:
            r, c, t = queue.popleft()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < m:# 지금 바로 방문 가능
                    if t >= moveTime[nr][nc]:
                        if t+1 < visited[nr][nc]:
                            visited[nr][nc] = t+1
                            queue.append((nr, nc, t+1))
                    else:# moveTime[nr][nc] 까지 기다려야 함
                        if moveTime[nr][nc]+1 < visited[nr][nc]:
                            visited[nr][nc] = moveTime[nr][nc]+1
                            queue.append((nr, nc, moveTime[nr][nc]+1))

        return visited[-1][-1]
                    


if __name__ == '__main__':
    cases = [
        [[0, 4], [4, 4]], # 6
        [[0, 0, 0], [0, 0, 0]], # 3
        [[0, 1], [1, 2]], # 3
        [[0, 100]], # 101
        [[0,58],[67,4]] # 60
    ]

    for case in cases:
        output = Solution().minTimeToReach(case)
        print(output)