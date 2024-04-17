# Bronze 3
# 1 <= N <= 10000, 1 <= K <= N
N, K = map(int, input().split())

array = [i for i in range(1, N+1)]
result = []

for n in array:
    if N % n == 0:
        result.append(n)

if K > len(result):
    print(0)
else:
    print(result[K-1])