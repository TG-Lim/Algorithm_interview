T = int(input())
array = [int(input()) for _ in range(T)]
namerji = int(1e9)+9

def solve(n: int):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2 # 2, 1+1
    dp[3] = 4 # 1+1+1 / 2+1 / 1+2 / 3

    for i in range(4, n+1):
        dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % namerji # 끝에 3 더하는 경우 , 끝에 2 더하는 경우, 끝에 1 더하는 경우
    
    return dp[n]

for n in array:
    print(solve(n))