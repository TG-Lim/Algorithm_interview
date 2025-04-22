from collections import deque
N, K = map(int, input().strip().split())
def hide_and_seek_with_path(N, K):
    MAX = 100000
    visited = [False] * (MAX+1)
    parent  = [-1]    * (MAX+1)
    dist    = [-1]    * (MAX+1)

    q = deque([N])
    visited[N] = True
    dist[N]    = 0

    while q:
        x = q.popleft()
        if x == K:
            break

        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not visited[nx]:
                visited[nx] = True
                parent[nx]  = x
                dist[nx]    = dist[x] + 1
                q.append(nx)

    # 1) 최소 시간
    print(dist[K])

    # 2) 경로 재구성
    path = []
    cur = K
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    print(*path)

hide_and_seek_with_path(N, K)