# Gold 5
# Simulation
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
array = list(map(int, input().split()))

stage = 0
fault = 0
robots = [False]*(2*N)

def stage_one():
    global array, robots
    array = [array[-1]] + array[:-1]

    robots = [False] + robots[:-1]
    robots[N-1] = False

def stage_two():
    global array, robots, fault
    for i in range(2*N-1, -1, -1):
        if robots[i] and not robots[i+1] and array[i+1] > 0: # 로봇이 있고, 다음 칸 내구도가 0보다 크고, 다음 칸에 로봇이 없는 경우
            robots[i+1] = True
            robots[i] = False # 로봇이 한칸 움직임
            array[i+1] -= 1

            if array[i+1] == 0: # 내구도가 0일 경우
                fault += 1
            
            if i+1 == N-1 and robots[i+1]: # 내리는 위치에서 내려야 함  
                robots[N-1] = False # 로봇은 내려야 함

def stage_three():
    global array, robots, fault
    if array[0] > 0: # 내구도가 0이 아닌 경우
        robots[0] = True
        array[0] -= 1
        
        if array[0] == 0: # 내구도가 0인 경우
            fault += 1

while fault < K:
    stage_one()
    stage_two()
    stage_three()

    stage += 1

print(stage)