import sys
sys.setrecursionlimit(10000)

def get_min_max_scratch(energy, scratch, memo):
    # 더 이상 분할 불가능
    if energy < 4:
        return scratch  # 흠집 수 반환

    key = (energy, scratch)
    if key in memo:
        return memo[key]

    min_max_scratch = float('inf')

    # 모든 분할 가능한 쌍 탐색
    for i in range(2, int(energy ** 0.5) + 1):
        if energy % i == 0:
            a = i
            b = energy // i
            # 각 분할 결과에 대해 재귀 호출
            max_scratch = max(
                get_min_max_scratch(a, scratch + 1, memo),
                get_min_max_scratch(b, scratch + 1, memo)
            )
            min_max_scratch = min(min_max_scratch, max_scratch)

    # 분할이 안 된 경우도 고려
    if min_max_scratch == float('inf'):
        min_max_scratch = scratch

    memo[key] = min_max_scratch
    return min_max_scratch

# 실행부
K = int(input())
memo = {}
print(get_min_max_scratch(K, 0, memo))