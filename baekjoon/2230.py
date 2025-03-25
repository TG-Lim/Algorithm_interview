import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
array = []

for _ in range(N):
    array.append(int(input()))

if N == 1: # 같은 수. 0 밖에 안 됨
    print(0)
    exit()

array.sort()

answer = int(1e12)

# 투 포인더 시작값 지정
start = 0
end = 1

while start <= end and end < len(array):
    diff = array[end] - array[start]
    if diff < M: # M 보다 커지도록 end 를 늘림
        end += 1
    else: # start 를 늘림
        answer = min(answer, diff)
        start += 1
        if start == end:
            end += 1

print(answer)