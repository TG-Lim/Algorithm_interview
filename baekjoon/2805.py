# Silver 2
import sys
N, M = map(int, input().strip().split())
array = list(map(int, sys.stdin.readline().strip().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for a in array:
        if a >= mid:
            total += (a-mid)
    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)