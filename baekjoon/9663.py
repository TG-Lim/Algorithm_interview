# Gold 4
# 백트레킹

N = int(input())

if N == 1:
    print(1)
    exit()

if N == 2 or N == 3:
    print(0)
    exit()

def check