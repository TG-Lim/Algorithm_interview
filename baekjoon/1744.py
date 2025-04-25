N = int(input())
stack = [int(input()) for _ in range(N)]

stack.sort()

answer = 0
last_number = None

# 양수들은 곱해서 더할 수 있는 만큼 더하기
while stack and stack[-1] > 1:
    p = stack.pop()
    if last_number is None:
        last_number = p
    else:
        answer += last_number*p
        last_number = None

if last_number is not None:
    answer += last_number
    last_number = None

# 1 처리. 1은 무조건 더하기
while stack and stack[-1] == 1:
    answer += stack.pop()

# 음수와 0은 작은 수 부터 처리
stack = stack[::-1]
while len(stack) >= 2:
    a = stack.pop()
    b = stack.pop()
    answer += a*b

if stack:
    answer += stack.pop()

print(answer)