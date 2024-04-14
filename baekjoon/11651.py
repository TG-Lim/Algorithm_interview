# Silver5
import sys
n = int(input())
positions = []
for _ in range(n):
    position = list(map(int, sys.stdin.readline().strip().split()))
    positions.append(position)

positions.sort(key=lambda x: (x[1], x[0]))

for i in range(n):
    end = '\n' if i < n-1 else ''
    temp = str(positions[i][0]) + ' ' + str(positions[i][1]) + end
    sys.stdout.write(temp)