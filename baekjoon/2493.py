import sys
input = sys.stdin.readline
N = int(input())
array = list(map(int, input().strip().split()))

stack = []
stack.append([1, array[0]]) # 인덱스, 탑의 높이

answer = [0]

for i in range(1, N):
    while stack:
        if stack[-1][1] >= array[i]: # 탑의 높이가 더 큼
            answer.append(stack[-1][0])
            stack.append([i+1, array[i]])
            break

        else: # 원래 오는 탑이 더 높음. 즉 빼야함
            stack.pop()

    if not stack: # 제일 높은 경우
        answer.append(0)
        stack.append([i+1, array[i]])

print(' '.join([str(a) for a in answer]))