import sys
input = sys.stdin.readline

n, W = map(int, input().strip().split())
prices = [int(input()) for _ in range(n)]

cnt = 0 # 비트코인 개수세기

for i in range(len(prices)-1):
    if prices[i] < prices[i+1]: # 사기
        cnt += W // prices[i]
        W %= prices[i]
    
    elif prices[i] > prices[i+1]: # 다 팔기
        W += cnt*prices[i]
        cnt = 0

if cnt > 0:
    W += prices[-1]*cnt
    cnt = 0

print(W)