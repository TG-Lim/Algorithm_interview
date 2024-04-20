# Silver 4
N, K = map(int, input().split())
array = []
for _ in range(N):
    array.append(int(input()))
array.sort(reverse=True)
answer = 0

for a in array:
    if K >= a:
        answer += K//a
        K -= a*(K//a)
print(answer)