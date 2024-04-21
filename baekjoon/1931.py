# Silver 1
# 1<= N <= 100,000 -> O(NlogN)
import sys
N = int(input())
array = []
for _ in range(N):
    array.append(list(map(int, sys.stdin.readline().rstrip().split())))
array.sort()

