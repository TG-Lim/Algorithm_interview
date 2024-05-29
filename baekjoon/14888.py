# Silver 2
import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().strip().split()))
initial_operator = list(map(int, input().strip().split()))

maximum = -int(1e9)
minimum = int(1e9)

def backtracking(number, cnt, operators):
    global maximum, minimum
    if cnt == N:
        maximum = max(maximum, number)
        minimum = min(minimum, number)
        return # 재귀함수 탈출용
    if operators[0] > 0:
        temp = operators[:]
        temp[0] -= 1
        backtracking(number+numbers[cnt], cnt+1, temp)
    if operators[1] > 0:
        temp = operators[:]
        temp[1] -= 1
        backtracking(number-numbers[cnt], cnt+1, temp)
    if operators[2] > 0:
        temp = operators[:]
        temp[2] -= 1
        backtracking(number*numbers[cnt], cnt+1, temp)
    if operators[3] > 0:
        temp = operators[:]
        temp[3] -= 1
        backtracking(int(number/numbers[cnt]), cnt+1, temp)
backtracking(numbers[0], 1, initial_operator)
print(maximum)
print(minimum)