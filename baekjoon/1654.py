# Silver 2, 이진탐색
K, N = map(int, input().split())
array = []
for _ in range(K):
    array.append(int(input()))
array.sort()
start = 1
end = array[-1]
best = 0

while start <= end:
    mid = (start+end)//2
    count = sum(a // mid for a in array)
    if count >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)