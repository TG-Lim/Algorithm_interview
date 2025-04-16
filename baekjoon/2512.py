N = int(input())
array = list(map(int, input().strip().split()))
budget = int(input())

array.sort()

start = 0
end = array[-1]

if sum(array) <= budget: # 모든 예산을 배정 가능
    print(array[-1])
    exit()

answer = -1

while start <= end:
    mid = int((start + end)/2)

    temp = sum([min(a, mid) for a in array]) # 예산 절감 되었을 때 지출
    if temp <= budget: # start를 조정해서 늘리기
        answer = max(answer, mid) # 예산 조절
        start = mid + 1
    else:
        end = mid - 1

print(answer)