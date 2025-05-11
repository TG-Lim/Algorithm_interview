import sys
sys.setrecursionlimit(int(1e9))
N, r, c = map(int, input().strip().split())

def find_number(N, r, c):
    if N == 0:
        return 0
    half = 2**(N-1)
    size = half*half

    if r < half and c < half:
        return 0 * size + find_number(N-1, r, c)
    elif r < half and c >= half:
        return 1 * size + find_number(N-1, r, c - half)
    elif r >= half and c < half:
        return 2 * size + find_number(N-1, r - half, c)
    else:
        return 3 * size + find_number(N-1, r - half, c - half)

answer = find_number(N, r, c)
print(answer)