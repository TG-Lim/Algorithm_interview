N, K, X = map(int, input().strip().split())
array = list(map(int, input().strip().split()))

start = 0
end = 0

money = sum(array[1:]) # len(array) >= 2
answer = -1

while start < N:
    vacation = end - start + 1
    if money >= K: # 돈 더 많음. -> 휴가 갈 수 있음
        answer = max(answer, vacation) # 휴가 조정
        if end < N-1:
            end += 1
            money -= array[end] # 현재 end 만큼 money 제거
        else:
            start += 1

    else: # 일 더 해야함
        start += 1
        money += X*array[start-1] # 빠진 만큼 더해주기

if answer <= 0:
    print(-1)
else:
    print(answer)