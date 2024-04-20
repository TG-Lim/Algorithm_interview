# Silver 4
# 1<= N <= 1000 -> O(N^2)
import sys
N = int(input())
array = list(map(int, sys.stdin.readline().split()))

array.sort()

result = sum([(len(array)-i) * array[i] for i in range(len(array))])
print(result)