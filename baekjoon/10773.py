# Silver 4
# 1<= K <= 100,000 -> O(NlogN)
import sys

K = int(input())
stack = []
for _ in range(K):
    k = int(sys.stdin.readline().strip())
    if k != 0:
        stack.append(k)
    else:
        stack.pop()
print(sum(stack))