# Gold 4
# N, M 50 이하 자연수
from collections import deque

N, M = map(int, input().strip().split())
know = list(map(int, input().strip().split()))
array = []
for _ in range(M):
    array.append(list(map(int, input().strip().split()))[1:])

if know[0] == 0:
    print(M)
    exit()

party = {i: [] for i in range(N+1)}
for m in range(M):
    for p in array[m]:
        party[p].append(m)


queue = deque([])
visited = [False]*(M+1)
true_know = know[1:]
cnt = 0
for t in true_know: # 진실을 아는 사람 목록
    for m in range(M):
        temp  = array[m]
        if t in temp and not visited[m]: # 진실을 아는 사람이 있는 경우
            visited[m] = True
            cnt += 1
            for p in temp:
                queue.append((m, p)) # 파티 index, 사람

while queue:
    party_index, person = queue.popleft()
    for p in party[person]: # 진실을 아는 사람이 간 파티는 다른 파티도 진실을 말해야 함
        if not visited[p]:
            visited[p] = True
            cnt += 1
            for person in array[p]:
                queue.append((p, person))

print(M-cnt)