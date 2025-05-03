from math import ceil
N, M = map(int, input().strip().split())
array = list(map(int, input().strip().split()))

threshold = ceil(0.9*M) # 구간 내 동일값의 개수

cnt = [0]*(int(1e6)+1) # 구간에서 개수 저장할 리스트
for i in range(M):
    cnt[array[i]] += 1

max_index = cnt.index(max(cnt))

if cnt[max_index] >= threshold:
    print('YES')
    exit()

answer = 'NO'

for i in range(1, N-M+1): # 1에서 N-M 까지
    cnt[array[i-1]] -= 1 # 나간 거 빼기
    cnt[array[i+M-1]] += 1 # 들어온 거 더하기

    if cnt[array[i+M-1]] > cnt[max_index]:
        max_index = array[i+M-1]
    
    if cnt[max_index] >= threshold:
        answer = 'YES'

print(answer)