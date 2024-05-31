from itertools import product

# Input
N = int(input())
M = int(input())
not_work = list(map(int, input().split())) if M != 0 else []
work = [i for i in range(10) if i not in not_work]

if M == 0: # 숫자 길이 또는 100에서 이동 시켰을 때 작은 값
    answer = min(abs(N-100), len(str(N)))
    print(answer)
    exit()

if M == 10: # +, - 누르는 횟수
    print(abs(N - 100))
    exit()

if N == 100:
    print(0)
    exit()

answer = abs(N - 100)

# 리모컨 누를 수 있는 조합들로 부터 가능한 조합 생성
for length in range(1, 7):
    for comb in product(work, repeat=length):
        channel = int(''.join(map(str, comb)))
        presses = len(str(channel)) + abs(N - channel)
        answer = min(answer, presses)

print(answer)