# Silver 3 자료구조
import sys
from collections import deque
test_case = int(input())
problems = []
docu_lists = []

for _ in range(test_case):
    problems.append(list(map(int, sys.stdin.readline().strip().split())))
    docu_lists.append(list(map(int, sys.stdin.readline().strip().split())))

def answer(problem:list , docu_list: list):
    queue = deque([])
    target_document = problem[1]
    docu_list_sorted = deque(sorted(docu_list, reverse=True))
    for i in range(problem[0]):
        queue.append((docu_list[i], i))
    cnt = 0
    while queue:
        v = queue.popleft() # v[0] : 중요도, v[1] : 문서 인덱스
        if v[0] < docu_list_sorted[0]: # 중요도 높은 문서가 하나라도 존재
            queue.append(v)
        else: # 없는 경우(출력)
            cnt += 1
            docu_list_sorted.popleft()

            if v[1] == target_document:
                break
    print(cnt)

for test in range(test_case):
    answer(problems[test], docu_lists[test])