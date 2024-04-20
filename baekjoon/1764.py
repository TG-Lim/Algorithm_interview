# Silver 4
import sys
N, M = map(int, input().split())
nodeut = []
nobot = []
for _ in range(N):
    nodeut.append(sys.stdin.readline().rstrip())
for _ in range(M):
    nobot.append(sys.stdin.readline().rstrip())

result = list(set(nodeut) & set(nobot))
result.sort()
print(len(result))
print('\n'.join(result))