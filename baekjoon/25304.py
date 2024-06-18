# Bronze 4

X = int(input())
N = int(input())
price = 0
for _ in range(N):
    p, n = map(int, input().strip().split())
    price += p*n

if price == X:
    print("Yes")
else:
    print("No")