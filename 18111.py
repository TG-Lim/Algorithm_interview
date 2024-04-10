# Silver2
# 1 <= M, N <= 500 -> O(N^3)
# 1 <= B <= int(6.4e7)

import sys
input = sys.stdin.readline
numbers = [0]*257
N, M, B = map(int, input().split())
for i in range(N):
    for j in list(map(int, input().split())):
        numbers[j] += 1

answer = int(1e10)
height = 0

def get_time(height):
    stack_num = 0
    pop_num = 0

    for i in range(257):
        n, tmp = numbers[i], i - height
        if n == 0:
            continue
        if tmp < 0: # 음수 인 경우 쌓아야 함
            stack_num += (-tmp)*n
        else:
            pop_num += tmp * n

    if (pop_num + B) >= stack_num:
        result = pop_num*2 + stack_num
        return result

    else:
        return 1e10


for h in range(257):
    result = get_time(h)
    if result <= answer:
        answer = result
        height = h

print(answer, height)