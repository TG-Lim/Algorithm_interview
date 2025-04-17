# ********** ㄹㅇ 고난도

X, Y = map(int, input().strip().split())

if X == Y:
    print(0)
    exit()

D = Y - X
k = int(D**0.5)

if k**2 == D:
    print(2*k-1)
    exit()

elif D <= k*(k+1):
    print(2*k)
    exit()
else:
    print(2*k+1)
    exit()