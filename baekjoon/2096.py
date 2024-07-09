# Gold 5

N = int(input())

max_prev = [0]*3
min_prev = [0]*3

for _ in range(N):
    temp = list(map(int, input().strip().split()))

    max_current = [0]*3
    min_current = [0]*3

    max_current[0] = max(max_prev[0:2]) + temp[0]
    max_current[1] = max(max_prev) + temp[1]
    max_current[2] = max(max_prev[1:]) + temp[2]

    min_current[0] = min(min_prev[0:2]) + temp[0]
    min_current[1] = min(min_prev) + temp[1]
    min_current[2] = min(min_prev[1:]) + temp[2]

    max_prev = max_current[:]
    min_prev = min_current[:]

print(max(max_prev), min(min_prev))