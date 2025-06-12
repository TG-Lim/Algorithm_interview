from typing import List
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1

        graph = [[] for _ in range(n)]
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        connected = 0
        visited = [False]*n

        def dfs(node):
            visited[node] = True
            for adj in graph[node]:
                if not visited[adj]:
                    dfs(adj)

        for node in range(n):
            if not visited[node]:
                dfs(node)
                connected += 1

        return connected-1

if __name__ == '__main__':
    cases = [
        [4, [[0,1],[0,2],[1,2]]],
        [6, [[0,1],[0,2],[0,3],[1,2],[1,3]]],
        [6, [[0,1],[0,2],[0,3],[1,2]]]
    ]

    for case in cases:
        output = Solution().makeConnected(case[0], case[1])
        print(output)