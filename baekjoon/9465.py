# Silver 1
import sys
T = int(input())
test_cases = []
for _ in range(T):
    n = int(input())
    temp = []
    for _ in range(2):
        temp.append(list(map(int, sys.stdin.readline().rstrip().split())))
    test_cases.append(temp)

def solution(test_case):
    n = len(test_case[0])
    dp = [[0]*n for _ in range(2)]
    dp[0][0] = test_case[0][0]
    dp[1][0] = test_case[1][0]

    if n>1:
        dp[0][1] = test_case[0][1] + dp[1][0]
        dp[1][1] = test_case[1][1] + dp[0][0]

    for i in range(2, n):
        dp[0][i] = test_case[0][i] + max(dp[1][i-1],dp[1][i-2])
        dp[1][i] = test_case[1][i] + max(dp[0][i-1],dp[0][i-2])
    print(max(dp[0][n-1], dp[1][n-1]))

for test_case in test_cases:
    solution(test_case)