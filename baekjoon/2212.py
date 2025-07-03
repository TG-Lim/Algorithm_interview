N = int(input())
K = int(input())

array = list(map(int, input().strip().split()))

if K >= N:
    print(0)
    exit()

array.sort()

if K == 1:
    print(array[-1] - array[0])
    exit()
    
delta = [array[i] - array[i-1] for i in range(1, N)]

delta.sort(reverse=True)

print(sum(delta[K-1:]))