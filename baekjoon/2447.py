import sys
sys.setrecursionlimit(10**7)

def make_star(n: int) -> list[str]:
    # 베이스 케이스: n == 3일 때
    if n == 3:
        return ['***',
                '* *',
                '***']
    # 1/3 크기의 패턴을 만들고
    half = n // 3
    prev = make_star(half)
    # 상단과 하단은 3번 반복
    top_bottom = [line * 3 for line in prev]
    # 중간 줄은 좌우에 prev, 가운데에 공백 블록
    middle = [line + ' ' * half + line for line in prev]
    # 합쳐서 반환
    return top_bottom + middle + top_bottom

def solve():
    N = int(sys.stdin.readline())
    pattern = make_star(N)
    # 한 번에 출력
    sys.stdout.write('\n'.join(pattern))
    
solve()