def solution():
    N = int(input())

    if N == 1:
        print(1)
        exit()

    dp = [0]*(N+1)

    dp[1] = 1
    dp[2] = 2


    for i in range(3, N+1):
        dp[i] = (dp[i-2] + dp[i-1]) % 15746
    
    print(dp[N] % 15746)

solution()