N, K = map(int, input().split())

denominator = 1
numerator = 1
for k in range(1, K+1):
    denominator *= k
    numerator *= (N-(k-1))

print(int(numerator/denominator))