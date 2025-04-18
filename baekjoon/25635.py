def solution():
    N = int(input())
    a = list(map(int, input().split()))
    S = sum(a)
    M = max(a)
    # 가능한 최대 이용 횟수
    result = S if M <= S - M + 1 else 2*(S - M) + 1
    print(result)

solution()