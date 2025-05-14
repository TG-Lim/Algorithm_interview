from collections import defaultdict
def reduce(x):
    seen = {}
    stack = [(x, 0)]

    while stack:
        val, d = stack.pop()

        if val in seen and seen[val] <= d:
            continue

        seen[val] = d

        if val == 1:
            continue

        left = val // 2
        right = val - left
        stack.append((left, d+1))
        stack.append((right, d+1))

    return seen


def solution(array):
    available = defaultdict(int)
    result = defaultdict(int)
    for a in array:
        seen = reduce(a)
        for number, cnt in seen.items():
            available[number] += 1
            result[number] += cnt

    temp = [result[a] for a in result if available[a] == N]

    return min(temp)

answers = []
T = int(input())
for _ in range(T):
    N = int(input())
    array = list(map(int, input().strip().split()))
    answer = solution(array)
    answers.append(answer)

print('\n'.join(str(answer) for answer in answers))