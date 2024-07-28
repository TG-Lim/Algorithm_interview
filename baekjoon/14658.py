# Gold 3
# 1 <= N, M <=  500,000, 1 <= L <= 100,000 , 1<= K <= 100
import sys
input = sys.stdin.readline

N, M, L, K = map(int, input().strip().split())

stars = []
for _ in range(K):
    x, y = map(int, input().strip().split())
    stars.append((x, y))

x_cands = set()
y_cands = set()
for x, y in stars:
    x_cands.add(x-L/2)
    x_cands.add(x+L/2)
    y_cands.add(y-L/2)
    y_cands.add(y+L/2)

answer = 100
for cx in x_cands:
    for cy in y_cands:
        temp = 0
        for x, y in stars:
            condition = (cx - L/2 <= x <= cx + L/2) and (cy - L/2 <= y <= cy + L/2)
            if condition: # 트램펄린으로 막아낼 수 있음
                temp += 1
        answer = min(answer, K-temp)

print(answer)