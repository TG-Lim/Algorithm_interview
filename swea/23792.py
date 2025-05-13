from typing import List
T = int(input())

def solution(array: List[int], N: int):
    ys = set()
    for a in array:
        ys.add(a)
        ys.add(a-0.1)
        ys.add(a+0.1)
    num_root = 0
    for y in ys:
        temp = 0
        for i in range(N-1):
            if array[i] == array[i+1] and array[i] == y: # 해가 무한대로 존재
                return -1
            elif (array[i] <= y < array[i+1]) or (array[i+1] < y <= array[i]): # 해가 존재
                temp += 1
            else:
                continue

        if y == array[-1]: # 마지막 부분 확인
            temp += 1

        num_root = max(num_root, temp)

    return num_root

answer = []
for _ in range(T):
    N = int(input())
    array = list(map(int, input().strip().split()))
    output = solution(array, N)
    answer.append(output)

print('\n'.join(str(a) for a in answer))