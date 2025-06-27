import sys
input = sys.stdin.readline

# 1 <= N <= 1e5 , 1 <= M <= 1e9

N, M = map(int, input().strip().split())

time_array = [int(input()) for _ in range(N)]

low = 1
high = min(time_array)*M
answer = high

while low <= high:
    mid = (low + high) // 2
    count = sum(mid//t for t in time_array)

    if count >= M:
        answer = mid
        high = mid - 1
    else:
        low = mid + 1

print(answer)