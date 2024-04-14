# Silver 5 구현
# 1 <= N <= 50 -> 시간복잡도 자유로움
N = int(input())
array = []
for _ in range(N):
    temp = list(map(int, input().strip().split()))
    array.append(temp)
ranks = []
for i in range(N):
    rank = 1
    for j in range(N):
        if i != j:
            condition = array[i][0] < array[j][0] and array[i][1] < array[j][1]
            if condition:
                rank += 1
    ranks.append(rank)

result = ' '.join([str(r) for r in ranks])
print(result)