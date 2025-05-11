N = int(input())
array = [list(map(int, input().strip().split())) for _ in range(N)]

cnt = [0, 0]

def all_same(x, y, size):
    initial = array[x][y]
    for r in range(x, x+size):
        for c in range(y, y+size):
            if array[r][c] != initial:
                return False
    
    return True

def compress(x, y, size):
    if all_same(x, y, size):
        cnt[array[x][y]] += 1    
    else:
        for i in range(2):
            for j in range(2):
                compress(x+i*size//2, y+j*size//2, size//2)

compress(0, 0, N)

print(cnt[0])
print(cnt[1])