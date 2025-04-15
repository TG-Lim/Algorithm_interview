import sys

input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split())) + [0, 0] # 마지막에서 길이 3 윈도우 용
dp = [0, array[0], array[0]+array[1]]

for i in range(2, N+2):
    # 마지막 + 스위치 안누르기 vs 세번째 이전 + 스위치 누르기
    dp.append(max(dp[-1]+array[i], dp[-3] + 2*(array[i-2] + array[i-1] + array[i])))
print(dp[-1])