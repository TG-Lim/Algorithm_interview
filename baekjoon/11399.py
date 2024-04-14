# Silver 4
import sys
N = int(input())
array = list(map(int, sys.stdin.readline().split()))

array.sort()
accum_sum = [0 for _ in range(N)]
for i in range(1,N):
    accum_sum[i] = accum_sum[i-1] + array[i]
print(accum_sum)