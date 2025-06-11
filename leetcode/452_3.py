from typing import List
from collections import deque
import heapq

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        R, C = len(classroom), len(classroom[0])
        
        # 1. 핵심 지점(S, L, R) 식별
        key_points = []
        start_idx = -1
        litter_map = {} # 쓰레기 좌표를 비트마스크 인덱스로 매핑
        point_to_idx = {}

        for r in range(R):
            for c in range(C):
                if classroom[r][c] != '.' and classroom[r][c] != 'X':
                    idx = len(key_points)
                    key_points.append((r, c))
                    point_to_idx[(r,c)] = idx
                    if classroom[r][c] == 'S':
                        start_idx = idx
                    elif classroom[r][c] == 'L':
                        litter_map[(r, c)] = len(litter_map)

        if start_idx == -1: return 0
        l_cnt = len(litter_map)
        if l_cnt == 0: return 0
        
        # 2. 핵심 지점 간 최단 거리 미리 계산
        def bfs_from_point(start_r, start_c):
            q = deque([(start_r, start_c, 0)])
            visited_bfs = {(start_r, start_c)}
            distances = {}
            while q:
                r, c, dist = q.popleft()
                if (r, c) in point_to_idx:
                    distances[point_to_idx[(r,c)]] = dist
                
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and classroom[nr][nc] != 'X' and (nr, nc) not in visited_bfs:
                        visited_bfs.add((nr, nc))
                        q.append((nr, nc, dist + 1))
            return distances

        adj = [[-1] * len(key_points) for _ in range(len(key_points))]
        for i, (r, c) in enumerate(key_points):
            distances = bfs_from_point(r, c)
            for j_idx, dist_val in distances.items():
                adj[i][j_idx] = dist_val

        # 3. 핵심 지점을 노드로 하는 그래프 탐색 (수정된 다익스트라 알고리즘)
        # 상태: (총 이동 횟수, -현재 에너지, 현재 위치 인덱스, 방문한 쓰레기 비트마스크)
        pq = [(0, -energy, start_idx, 0)] 
        visited = {} # visited[(위치 인덱스, 방문 마스크)] = 최소 이동 횟수
        
        final_mask = (1 << l_cnt) - 1

        while pq:
            moves, neg_e, u_idx, mask = heapq.heappop(pq)
            e = -neg_e

            if (u_idx, mask) in visited and moves >= visited[(u_idx, mask)]:
                continue
            visited[(u_idx, mask)] = moves

            if mask == final_mask:
                return moves

            for v_idx in range(len(key_points)):
                if u_idx == v_idx or adj[u_idx][v_idx] == -1:
                    continue

                dist_to_v = adj[u_idx][v_idx]
                
                if e >= dist_to_v:
                    new_moves = moves + dist_to_v
                    new_energy = e - dist_to_v
                    new_mask = mask
                    
                    v_point = key_points[v_idx]
                    
                    if v_point in litter_map:
                        litter_bit = litter_map[v_point]
                        new_mask |= (1 << litter_bit)
                    
                    if classroom[v_point[0]][v_point[1]] == 'R':
                        new_energy = energy
                    
                    heapq.heappush(pq, (new_moves, -new_energy, v_idx, new_mask))

        return -1

if __name__ == '__main__':
    cases = [
        [["S.", "XL"], 2], # 2
        [["LS", "RL"], 4], # 3
        [["L.S", "RXL"], 3], # -1
        [["LRLRXX", "R.R.LL", "L...R.", ".RL.XL", "X.XRRR", ".L.RXL", "...SLX", ".RXX.R", "..XR.."], 10], # 40
        [[".LL.", "SX.R", "L.RX", "X..L"], 13], # 9
    ]

    for case in cases:
        output = Solution().minMoves(case[0], case[1])
        print(output)