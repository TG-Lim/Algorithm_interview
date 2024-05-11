# Gold 5
# 1 <= p <= 100,000 -> O(NlogN)
import sys
from collections import deque

T = int(input())

for i in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    array = sys.stdin.readline().rstrip()[1:-1].split(',')
    queue = deque(array)
    flip = 0
    okay = True
    if n == 0:
        queue = []
        flip = 0
    for c in p:
        if c == 'R':
            flip += 1
        elif c == 'D':
            if not queue:
                print("error")
                okay = False
                break
            else:
                if flip % 2 == 1: # 한번 뒤집으면 뒤에서 나감
                    queue.pop()
                else:
                    queue.popleft()
    if okay:
        if flip % 2 == 0:
            print('['+",".join(queue)+"]")
        else:
            queue.reverse()
            print("["+",".join(queue)+"]")