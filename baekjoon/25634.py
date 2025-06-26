N = int(input())
array = list(map(int, input().strip().split()))
onoff = list(map(int, input().strip().split()))

if N == 1:
    print(array[0]*(1-onoff[0]))
    exit()

correct = [array[0]*onoff[0]]
for i in range(1, N):
    correct.append(correct[-1] + array[i]*onoff[i])

g = [array[i]*(1 - 2*onoff[i]) for i in range(N)]

# 3) Kadane으로 최대 연속 부분합(max_gain) 계산
max_ending = g[0]
max_gain   = g[0]
for i in range(1, N):
    max_ending = max(g[i], max_ending + g[i])
    max_gain   = max(max_gain, max_ending)

# 4) 결과 출력
print(correct[-1] + max_gain)