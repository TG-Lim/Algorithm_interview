# Silver 2 Dynamic Programming
# n <= 100,000 -> O(NlogN)
import sys
n = int(input())
array = list(map(int, sys.stdin.readline().strip().split()))

for i in range(1, n):
    array[i] = max(array[i], array[i-1] + array[i])

print(max(array))