from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        m, n = len(image), len(image[0])
        visited = [[False]*n for _ in range(m)]
        visited[sr][sc] = True
        start_color = image[sr][sc]
        image[sr][sc] = color
        queue = deque([(sr, sc)])

        while queue:
            r, c = queue.popleft()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and image[nr][nc] == start_color:
                    visited[nr][nc] = True
                    image[nr][nc] = color
                    queue.append((nr, nc))

        return image

if __name__ == '__main__':
    cases = [([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2),
             ([[0,0,0],[0,0,0]], 0, 0, 0),
             ([[1, 1], [1, 1]], 1, 1, 3)]

    for case in cases:
        solution = Solution()
        print(solution.floodFill(image=case[0], sr=case[1], sc=case[2], color=case[3]))