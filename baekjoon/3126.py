import sys
input = sys.stdin.readline

# Read input
xm, ym, xb, yb = map(int, input().strip().split())
N = int(input())
array = list(input().strip())
array = [int(a) for a in array]

# Eight directions: [up, up-left, left, down-left, down, down-right, right, up-right]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

# Step 1: Compute original directions and positions
d = [0] * N
d[0] = array[0] % 8
for n in range(1, N):
    d[n] = (d[n-1] + array[n]) % 8

pos = [(xm, ym)]  # pos[k] is position before step k
for n in range(N):
    x, y = pos[-1]
    x += dx[d[n]]
    y += dy[d[n]]
    pos.append((x, y))

# Step 2: Compute frequency of directions from each step to end
freq = [[0] * 8 for _ in range(N + 1)]
for n in range(N - 1, -1, -1):
    freq[n] = freq[n + 1].copy()
    freq[n][d[n]] += 1

# Step 3: Compute original distance (no commands ignored)
answer = ((pos[N][0] - xb) ** 2 + (pos[N][1] - yb) ** 2) ** 0.5

# Step 4: For each step k, try ignoring the command and using a different one
for k in range(N):
    for offset in range(1, 8):  # Offset 1 to 7 ensures new_cmd != array[k]
        mx = my = 0
        # Compute movement sum from step k to N-1 with shifted directions
        for dir in range(8):
            new_dir = (dir + offset) % 8
            mx += freq[k][dir] * dx[new_dir]
            my += freq[k][dir] * dy[new_dir]
        # New position after changing command at step k
        new_x = pos[k][0] + mx
        new_y = pos[k][1] + my
        dist = ((new_x - xb) ** 2 + (new_y - yb) ** 2) ** 0.5
        answer = min(answer, dist)

# Output the minimum distance
print(answer)