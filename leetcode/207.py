from collections import defaultdict
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        have_to_visit = [0]*numCourses
        visited = [False]*numCourses
        graph = defaultdict(set)

        for a, b in prerequisites:
            # 방문해야하는 도시 추가
            graph[a].add(b)
            have_to_visit[a] += 1
        
        def dfs(node: int):
            visited[node] = True
            for key, value in graph.items():
                if node in value:
                    graph[key].remove(node)
                    have_to_visit[key] -= 1
                
                if have_to_visit[key] == 0 and not visited[key]:
                    dfs(key)
            
            return
        
        for node in range(numCourses):
            if have_to_visit[node] == 0 and not visited[node]:
                dfs(node)
    
        if False in visited:
            return False
        else:
            return True


if __name__ == '__main__':
    cases = [
        [2, [[1,0]]],
        [2, [[1,0],[0,1]]]
    ]

    for case in cases:
        output = Solution().canFinish(case[0], case[1])
        print(output)