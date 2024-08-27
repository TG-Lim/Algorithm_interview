# Gold 4
import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())

grids = {}
for i in range(1, N+1):
    for j in range(1, N+1):
        grids[(i, j)] = deque([])

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    grids[(r, c)].append((m, s, d, 0)) # 질량, 속력, 방향, 시간

def move(k):
    for position in grids.keys():
        if len(grids[position]) > 0:
            for _ in range(len(grids[position])):
                m, s, d, t = grids[position].popleft()
                if t == k: # 원래부터 있던 파이어볼
                    nr, nc = position[0] + dr[d]*s, position[1] + dc[d]*s
                    if nr > N:
                        nr = (nr % N)
                        if nr == 0:
                            nr = N
                    if nc > N:
                        nc = (nc % N)
                        if nc == 0:
                            nc = N
                    if nr < 1:
                        nr = N-((-nr) % N)
                    if nc < 1:
                        nc = N-((-nc) % N)    
                    grids[(nr, nc)].append((m, s, d, t+1))
                else:
                    grids[position].append((m, s, d, t))

def combine():
    for position in grids.keys():
        if len(grids[position]) > 1: # 2개 이상의 파이어볼이 있음
            total_mass = 0
            total_speed = 0
            num_odd = 0
            num_even = 0
            for fireball in grids[position]:
                total_mass += fireball[0]
                total_speed += fireball[1]

                if fireball[2] % 2 == 0: # 방향이 짝수
                    num_even += 1
                else: # 방향이 홀수
                    num_odd += 1
    
            m = int(total_mass/5)
            s = int(total_speed/len(grids[position]))
            t = fireball[3]

            if m > 0: # 질량이 0보다 큰 경우
                if num_even == len(grids[position]) or num_odd == len(grids[position]): # 전부 방향이 짝수거나 홀수
                    grids[position] = deque([(m, s, 0, t), (m, s, 2, t), (m, s, 4, t), (m, s, 6, t)]) # 0, 2, 4, 6 방향
                else:
                    grids[position] = deque([(m, s, 1, t), (m, s, 3, t), (m, s, 5, t), (m, s, 7, t)]) # 0, 2, 4, 6 방향
            
            else:
                grids[position] = deque([])


def answer():
    total = 0
    for position in grids.keys():
        if len(grids[position]) > 0:
            for fireball in grids[position]:
                total += fireball[0]
    
    print(total)

for k in range(K):
    move(k)
    combine()

answer()