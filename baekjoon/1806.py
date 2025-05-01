import sys
input = sys.stdin.readline

N, S = map(int, input().strip().split())
array = list(map(int, input().strip().split()))

start = 0
end = 0
answer = int(1e6)

part_sum = array[0]

while start <= end:
    if part_sum < S: # 합이 작음
        if end < N-1:
            end += 1
            part_sum += array[end]
            continue

    else: # 합이 큼
        answer = min(answer, end - start + 1)
        part_sum -= array[start]
        start += 1
        continue

    # 아무런 것도 안했을 때 루프 탈출용 조절
    start += 1

if answer == int(1e6): # 불가능함
    print(0)
    exit()
print(answer)