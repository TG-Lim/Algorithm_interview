import sys
input = sys.stdin.readline

M, N = map(int, input().strip().split())
snacks = list(map(int, input().strip().split()))
max_snack = sum(snacks)//M

result = 0

left = 1
right = max_snack

while left <= right:
    mid = (left+right)//2
    total_cnt = sum(s // mid for s in snacks)
    if total_cnt >= M: # 더 긴 길이로 탐색
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)