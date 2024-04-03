# Bronze 2

N = int(input())
limit = 1000000

for i in range(1,limit+1):
    part_list = list(map(int, list(str(i))))
    temp = i + sum(part_list)
    if temp == N:
        print(i)
        exit()
print(0)