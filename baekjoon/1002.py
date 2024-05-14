# Silver 3
# Math
import sys
T = int(input())

def solve(x1, y1, r1, x2, y2, r2):
    d = (x1-x2)**2 + (y1-y2)**2
    if d > (r1+r2)**2:
        return 0
    elif d == (r1+r2)**2:
        return 1
    elif (r1-r2)**2 < d < (r1+r2)**2:
        return 2
    elif d == (r1-r2)**2:
        if x1 == x2 and y1 == y2:
            return -1
        else:
            return 1
    elif d < (r1-r2)**2 and (r1 != r2):
        return 0

result = []
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().strip().split())
    result.append(solve(x1, y1, r1, x2, y2, r2))

print('\n'.join(str(r) for r in result))