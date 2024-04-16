# Silver 4
import sys
N, M = map(int, input().split())
memo = {}
for i in range(N):
    site, password = sys.stdin.readline().strip().split()
    memo[site] = password
for _ in range(M):
    site = sys.stdin.readline().strip()
    sys.stdout.write(memo[site]+'\n')