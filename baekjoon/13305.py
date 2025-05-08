import sys
input = sys.stdin.readline

N = int(input())
roads = list(map(int, input().strip().split()))
oils = list(map(int, input().strip().split()))

# roads[i]: 0~i 번째 oils 까지 기름 채울 수 있음
# 즉 roads 전까지 어디가 최소인 지 구할 것

min_oils = [None]*len(roads)

min_oil_price = int(1e10)
for i in range(len(roads)):
    if oils[i] < min_oil_price:
        min_oil_price = oils[i]
    min_oils[i] = min_oil_price

price = 0
for i in range(len(roads)):
    price += min_oils[i]*roads[i]

print(price)