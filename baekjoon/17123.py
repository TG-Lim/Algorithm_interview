import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    R, C = N, len(arr[0])
    
    # 1) (R+1)x(C+1) 크기의 0 차분 배열 준비
    diff = [[0]*(C+1) for _ in range(R+1)]
    
    # 2) 각 업데이트를 O(1)로 기록
    #    (r1,c1)~(r2,c2)에 v 더하기
    for _ in range(M):
        r1, c1, r2, c2, v = map(int, input().split())
        r1 -= 1; c1 -= 1  # 0-based index
        # 차분 배열 네 군데에만 더하고 빼면,
        diff[r1][c1]     += v
        diff[r1][c2]     -= v
        diff[r2][c1]     -= v
        diff[r2][c2]     += v
    
    # 3) 2D 누적합으로 diff를 실제 더해 줄 값으로 바꾼 뒤 arr에 반영
    for i in range(R):
        for j in range(C):
            if i > 0: diff[i][j] += diff[i-1][j]
            if j > 0: diff[i][j] += diff[i][j-1]
            if i > 0 and j > 0: diff[i][j] -= diff[i-1][j-1]
            arr[i][j] += diff[i][j]
    
    # 4) 행 합과 열 합을 출력
    #    행 합
    row_sums = [ str(sum(row)) for row in arr ]
    #    열 합
    col_sums = []
    for j in range(C):
        s = 0
        for i in range(R):
            s += arr[i][j]
        col_sums.append(str(s))
    
    print(' '.join(row_sums))
    print(' '.join(col_sums))
