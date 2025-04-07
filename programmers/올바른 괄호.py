from collections import deque

def solution(s):
    queue = deque(list(s))
    cnt = 0
    while queue:
        letter = queue.popleft()
        if letter == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt < 0:
            return False
    if cnt == 0:
        return True
    else:
        return False