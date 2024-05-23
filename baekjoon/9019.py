# Gold 4
# BFS
import sys
from collections import deque

def function_D(number: int):
    return 2*number % 10000

def function_S(number: int):
    if number == 0:
        return 9999
    else:
        return number-1

def function_L(number: int):
    if len(str(number)) != 4:
        n = len(str(number))
        number_str = "0"*(4-n)+str(number)
    else:
        number_str = str(number)
    new_number = number_str[1:] + number_str[0]
    return int(new_number)

def function_R(number: int):
    if len(str(number)) != 4:
        n = len(str(number))
        number_str = "0"*(4-n)+str(number)
    else:
        number_str = str(number)
    new_number = number_str[3] + number_str[0:3]
    return int(new_number)

functions = ["D", "S", "L", "R"]

def bfs(input_number, target_number):
    visited = [False]*(10001)
    queue = deque([(input_number, [])])
    visited[input_number] = True
    while queue:
        number, commend = queue.popleft()
        for i in range(4):
            if functions[i] == "D":
                newnum = function_D(number)
            if functions[i] == "S":
                newnum = function_S(number)
            if functions[i] == 'L':
                newnum = function_L(number)
            if functions[i] == "R":
                newnum = function_R(number)
            if newnum == target_number:
                return commend + [functions[i]]
            else:
                if not visited[newnum]:
                    visited[newnum] = True
                    queue.append((newnum, commend+[functions[i]]))

input = sys.stdin.readline
T = int(input())
results = []
for _ in range(T):
    input_number, target_number = map(int, input().strip().split())
    result = ''.join(bfs(input_number, target_number))
    results.append(result)
print('\n'.join(results))