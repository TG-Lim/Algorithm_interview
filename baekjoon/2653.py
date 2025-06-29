import sys
from typing import List
input = sys.stdin.readline

n = int(input())
array = [[0] for _ in range(n+1)]

for i in range(1, n+1):
    array[i].extend(list(map(int, input().strip().split())))
    
groups = []

## 서로 좋아하는 사람들끼리 일단 묶기
visited = [False]*(n+1)

for node in range(1, n+1):
    if not visited[node]:
        visited[node] = True
        group = [node]
        for adj_node in range(1, n+1):
            if node == adj_node:
                continue
            if array[node][adj_node] == 0: # 좋아함
                group.append(adj_node)
                visited[adj_node] = True
        groups.append(group)
        
# 모든 소그룹이 2명이상인 지 확인
for group in groups:
    if len(group) < 2:
        print(0)
        exit()

num_groups = len(groups)
for i in range(num_groups):
    for j in range(i+1, num_groups):
        for node in groups[i]:
            for other_node in groups[j]:
                if array[node][other_node] == 0: # 다른 그룹에서 좋아하는 사람 있음 -> 안정된 집단이 아님
                    print(0)
                    exit()

groups.sort(key=lambda x: (x[0]))

print(len(groups))
for group in groups:
    group.sort()
    print(' '.join(str(node) for node in group))