# Silver 5
seed = int(input())
stock = list(map(int, input().split()))

# BNP
money = seed
stock_cnt = 0
for a in stock:
    if money >= a:
        stock_cnt += (money//a)
        money -= (a*(money//a))
BNP = money + stock_cnt*stock[-1]

# TIMING
money = seed
stock_cnt = 0
for i in range(3,14):
    if (stock[i] > stock[i-1]) & (stock[i-1] > stock[i-2]) & (stock[i-2] > stock[i-3]) & (stock_cnt > 0): # 매도 조건
        money += stock_cnt*stock[i]
        stock_cnt = 0
    if (stock[i] < stock[i-1]) & (stock[i-1] < stock[i-2]) & (stock[i-2] < stock[i-3]) & (money >= stock[i]): # 매수 조건
        stock_cnt += (money//stock[i])
        money -= stock[i]*(money//stock[i])
TIMING = money + (stock_cnt*stock[-1])

if BNP > TIMING:
    print("BNP")
elif BNP < TIMING:
    print("TIMING")
else:
    print("SAMESAME")