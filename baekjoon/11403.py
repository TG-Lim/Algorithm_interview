# Silver 1
# 1 <= N <= 100 -> O(N^3)
# 모든 지점에서 다른 지점 까지 경로 고려 -> 플로이드-워셜 알고리즘

N = int(input())
adjacent_matrix = []
for _ in range(N):
    adjacent_matrix.append(list(map(int, input().rstrip().split())))
result = [[0]*N for _ in range(N)]

# 초기 설정
for i in range(N):
    for j in range(N):
        if adjacent_matrix[i][j] == 1:
            result[i][j] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if result[i][k] == 1 and result[k][j] == 1:
                result[i][j] = 1

for r in result:
    string_list = list(map(str, r))
    print(' '.join(string_list))