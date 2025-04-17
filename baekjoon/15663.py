N, M = map(int, input().strip().split())
array = list(map(int, input().strip().split()))
array.sort()  # 사전 순 정렬 보장

from itertools import permutations

# 중복 제거를 위해 set 사용
result = set(permutations(array, M))

# 사전 순 정렬
result = sorted(result)

# 출력
for perm in result:
    print(' '.join(map(str, perm)))