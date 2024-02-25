import itertools
import sys

arr = [str(i) for i in range(1, 10)]
nPr = list(itertools.permutations(arr, 3))

nPr = [''.join(s) for s in nPr]

n = int(sys.stdin.readline())

numbers = []
strikes = []
balls = []

for _ in range(n):
    number, strike, ball = sys.stdin.readline().split()
    numbers.append(number)
    strikes.append(int(strike))
    balls.append(int(ball))


def get_strike(answer: str, answer_cand: str):
    cnt = 0
    for i in range(3):
        if answer[i] == answer_cand[i]:
            cnt += 1
    return cnt

def get_ball(answer: str, answer_cand: str):
    cnt = 0
    for s in answer_cand:
        if s in answer and answer.find(s) != answer_cand.find(s): # 같을경우 strike
            cnt += 1
    return cnt

result = 0
for answer in nPr: # answer가 정답일때
    temp = 0
    for i in range(n):
        answer_cand = numbers[i]
        strike = strikes[i]
        ball = balls[i]

        strike_cal = get_strike(answer, answer_cand)
        ball_cal = get_ball(answer, answer_cand)

        if strike == strike_cal and ball == ball_cal:
            temp += 1
    if temp == n:
        result += 1

print(result)