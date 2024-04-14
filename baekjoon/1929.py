import sys
m, n = map(int, sys.stdin.readline().split())
array = [False, False] + [True]*(n-1)
primes = []

for i in range(2, n+1):
    if array[i]:
        if i >= m:
            primes.append(i)
        for j in range(2*i, n+1, i): # 그 수의 2배부터 끝까지 소수의 배수들을 제거
            array[j] = False

for prime in primes:
    print(prime)