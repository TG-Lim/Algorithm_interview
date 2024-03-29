# Silver 4, 정렬
import sys
N = int(input())
array = set(map(int, sys.stdin.readline().strip().split()))

M = int(input())
find_array = list(map(int, sys.stdin.readline().strip().split()))

for i in range(M):
    a = find_array[i]
    end = "\n" if i < M-1 else ""
    if a in array:
        result = str(1)+end
    else:
        result = str(0)+end
    sys.stdout.write(result)