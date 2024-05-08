# Gold 5
# Brute Force
N = int(input())
M = int(input())
not_work = list(map(int, input().split()))
work = [i for i in range(1,10) if i not in not_work]

start = 100
cnt = 0

if N == start:
    print(0)
    exit()

