N = int(input())
size_list = list(map(int, input().strip().split()))
T, P = map(int, input().strip().split())

tshirt = 0
for s in size_list:
    if 0< s < T:
        tshirt += 1
    if s >= T:
        if s % T == 0:
            tshirt += s//T
        else:
            tshirt += ((s//T)+1)
print(tshirt)
print(N//P, N%P)