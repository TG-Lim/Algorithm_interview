import sys
from collections import deque

input = sys.stdin.readline

def button_A(n: int):
    if n < 99999:
        return n+1
    else:
        return -1
    
def button_B(n: int):
    if n >= 50000: # 2배하면 넘어감
        return -1
    else:
        n *= 2
        temp = list(str(n))
        temp[0] = str(int(temp[0]) - 1)
        return int(''.join(temp))

N, T, G = map(int, input().strip().split())
visited = [False]*100000 # 0 ~ 99999
visited[N] = True
queue = deque([])
queue.append((N, 0)) # 숫자, 버튼 누른 횟수

while queue:
    number, turn = queue.popleft()
    if number == G:
        print(turn)
        exit()
    a_num = button_A(number)
    b_num = button_B(number)

    if a_num > -1 and not visited[a_num] and turn < T:
        visited[a_num] = True
        queue.append((a_num, turn+1))
    if b_num > -1 and not visited[b_num] and turn < T:
        visited[b_num] = True
        queue.append((b_num, turn+1))

print('ANG')