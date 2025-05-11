N = int(input())
array = [list(map(int, input().strip().split())) for _ in range(N)]

cnt = {
    -1: 0,
    0: 0,
    1: 0
}

def is_same(x, y, size):
    initial = array[x][y]
    for r in range(x, x+size):
        for c in range(y, y+size):
            if array[r][c] != initial:
                return False
    
    return True

def compress(x, y, size):
    if is_same(x, y, size):
        cnt[array[x][y]] += 1
        return
    
    else:
        size = size//3
        for i in range(3):
            for j in range(3):
                compress(x+i*size, y+j*size, size)

compress(0, 0, N)

for value in cnt.values():
    print(value)