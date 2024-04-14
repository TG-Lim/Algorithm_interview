# Silver 3 DP

import sys
n = int(sys.stdin.readline())
array = [0 for _ in range(1001)]
array[1] = 1
array[2] = 2
for i in range(3, 1001):
    array[i] = array[i-1] + array[i-2]

print(array[n]%10007)