# Gold 5
import sys
input = sys.stdin.readline

T, W = map(int, input().split())
jadus = [0]
for _ in range(T):
    jadus.append(int(input()))


array = [[0]*(W+1) for _ in range(T+1)]
locations = [[0]*(W+1) for _ in range(T+1)] # locations[t][w]: 시점 t 에서 위치를 w 번 바꿨을 때 위치

locations[1][0] = 1
locations[1][1] = 2

for t in range(T+1):
    locations[t][0] = 1

array[1][0] = 1 if jadus[1] == 1 else 0
array[1][1] = 0 if jadus[1] == 2 else 1

for t in range(2, T+1):
    if jadus[t] == 1:
        c = 1
    else:
        c = 0
    array[t][0] = array[t-1][0] + c

def change_location(position):
    if position == 1:
        return 2
    if position == 2:
        return 1

for t in range(2, T+1):
    for w in range(1, min(31, W+1)): # 30 번 넘어가면 자동으로 30, 아니면 현재 시점까지
        new_position = change_location(locations[t-1][w-1])
        locations[t][w] = new_position

    for w in range(1, min(31,W+1)):
        if locations[t][w] == jadus[t]: # 자두를 받아먹을 수 있음
            array[t][w] = max(array[t-1][w-1], array[t-1][w]) + 1 # 자리 바꾼 경우와 자리 안바꾼 경우 중 더 많이 먹은 케이스
        else:
            array[t][w] = max(array[t-1][w-1], array[t-1][w])


print(max(array[-1]))