N = int(input())
array = [list(input().strip()) for _ in range(N)]

def is_uniform(x, y, size): # 영역 같은 지 확인하는 함수
    initial = array[x][y]
    for r in range(x, x+size):
        for c in range(y, y+size):
            if initial != array[r][c]:
                return False
    
    return True

def compress(x: int, y: int, size: int):
    
    if is_uniform(x, y, size): # 전부 다 일치하는 경우
        return str(array[x][y])
    
    else:
        a = compress(x, y, size//2)
        b = compress(x, y+size//2, size//2)
        c = compress(x+size//2, y, size//2)
        d = compress(x+size//2, y+size//2, size//2)

        return f'({a}{b}{c}{d})'
    

answer = compress(0, 0, N)
print(answer)