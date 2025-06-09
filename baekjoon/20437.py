from typing import List
from collections import defaultdict

def solution(W: str, K: int) -> List[int]:
    counter = defaultdict(list)
    for i, string in enumerate(W):
        counter[string].append(i)
    answer = []

    third_answer = 10001
    fourth_answer = 0
    for value in counter.values():
        if len(value) < K: # 조건 만족 못함
            continue

        for i in range(len(value)-(K)+1):
            length = value[i+K-1] - value[i] + 1
            third_answer = min(third_answer, length)
            fourth_answer = max(length, fourth_answer)

    if third_answer == 10001:
        answer.append(-1)
    else:
        answer.append(third_answer)

    if fourth_answer == 0:
        answer.append(-1)
    else:
        answer.append(fourth_answer)

    if answer[0] == -1 and answer[1] == -1:
        return [-1]
    else:
        return answer

T = int(input())
for _ in range(T):
    W = input().strip()
    K = int(input())
    output = solution(W, K)

    print(' '.join([str(l) for l in output]))