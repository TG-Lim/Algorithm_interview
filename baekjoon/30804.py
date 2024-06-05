# Silver 2
# 1 <= N <= 200000
import sys
sys.setrecursionlimit(int(1e9))

N = int(input())
array = list(map(int, input().strip().split()))

nums = [0]*10

def two_point(N, array, left, right, cnt, kind, max_count):
    if right >= N:
        return max_count
    
    if nums[array[right]] == 0:
        kind += 1
    
    cnt += 1
    nums[array[right]] += 1
    
    if kind > 2:
        if nums[array[left]] == 1:
            kind -= 1
        nums[array[left]] -= 1
        cnt -= 1
        left += 1
    
    max_count = max(max_count, cnt)
    
    return two_point(N, array, left, right+1, cnt, kind, max_count)

print(two_point(N, array, 0, 0, 0, 0, 0))