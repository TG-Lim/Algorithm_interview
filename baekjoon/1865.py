import sys
input = sys.stdin.readline
inf = int(1e9)

def bf(n, edges, dist):
    for i in range(n): # 모든 vertex
        for j in range(len(edges)): # 모든 edge
            cur, next, cost = edges[j] # 출발, 도착, 비용
            if dist[next] > dist[cur] + cost: # 현재 시점 도착 비용이 다른 edge 거쳐서 가는 것 보다 클때 갱신
                dist[next] = dist[cur]+cost
                if i == n-1: # 음의 사이클 존재
                    return True
                
    return False

TC = int(input())
answers = []
for _ in range(TC):
    n, m, w = map(int, input().strip().split())
    edges = []
    dist = [inf]*(n+1)

    for i in range(m+w): # 모든 edge 개수만큼 받아오기
        s, e, t = map(int, input().split())
        if i >= m:
            t *= -1
        else:
            edges.append((e, s, t)) # 도로는 양방향, # 웜홀은 단방향
        edges.append((s, e, t))
    
    if bf(n, edges, dist):
        answers.append("YES")
    else:
        answers.append("NO")

print("\n".join(answers))