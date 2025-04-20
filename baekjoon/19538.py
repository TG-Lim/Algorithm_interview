import sys
from collections import deque

def solution():
    input = sys.stdin.readline

    N = int(input())
    # 그래프 인접 리스트 생성 (리스트 사용)
    E = [[] for _ in range(N+1)]
    for u in range(1, N+1):
        data = list(map(int, input().split()))
        data.pop()  # 마지막 0 제거
        for v in data:
            E[u].append(v)
            E[v].append(u)

    M = int(input())
    initial = list(map(int, input().split()))
    # 결과 배열: rumors[i] = i번 사람이 루머를 믿는 시간, 초기엔 -1
    rumors = [-1] * (N+1)
    # 각 노드가 루머를 믿기 위해 필요한 최소 믿음 수 (ceil(deg/2))
    need = [0] * (N+1)
    for i in range(1, N+1):
        deg = len(E[i])
        need[i] = (deg + 1) // 2

    # 현재까지 이웃 중 루머를 믿는 사람 수 카운터
    cnt = [0] * (N+1)

    q = deque()
    # 최초 유포자 설정
    for x in initial:
        rumors[x] = 0
        q.append(x)

    # BFS
    while q:
        u = q.popleft()
        for v in E[u]:
            if rumors[v] != -1:
                # 이미 루머 믿고 있으면 패스
                continue
            cnt[v] += 1
            # 이웃 중 믿는 사람이 절반 이상이면
            if cnt[v] >= need[v]:
                rumors[v] = rumors[u] + 1
                q.append(v)

    # 출력
    print(' '.join(map(str, rumors[1:])))

solution()