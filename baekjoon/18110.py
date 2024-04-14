# Silver 2
import sys

eps = 0.00000001
array = []
n = int(input())
for _ in range(n):
    array.append(int(sys.stdin.readline()))
if n == 0:
    print(0)
    exit()
array.sort()

bound = round(0.15*n+eps)
part_array = array[bound:n-bound]
print(round(sum(part_array)/len(part_array) + eps))
