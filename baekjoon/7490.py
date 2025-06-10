from typing import List
from collections import deque

def solution(N: int) -> List[str]:
    result = []    
    queue = deque([['1']])
    while queue:
        num = queue.popleft()
        if num[-1] == str(N): # 마지막 숫자까지 탐색
            temp = ''.join(n for n in num if n != ' ')
            if eval(temp) == 0: # 0 인 경우 결과 추가
                result.append(''.join(n for n in num))
            continue

        for operator in ['+', '-', ' ']:
            new_num = num[:]
            new_num.append(operator)
            if int(new_num[-2]) < N:
                new_num.append(str(int(new_num[-2])+1))
                queue.append(new_num)
    result.sort()
    return result

answer = []
T = int(input())
for _ in range(T):
    N = int(input())
    result = solution(N)
    answer.extend(result)
    answer.append('')

for a in answer[:-1]:
    print(a)