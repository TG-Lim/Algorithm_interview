H, W, N, M = map(int, input().strip().split())

row = [False]*H
for i in range(0, H, N+1):
    row[i] = True

col = [False]*W

for i in range(0, W, M+1):
    col[i] =  True

print(sum(row)*sum(col))