# Silver 3 수학
# 1 <= N <= 500,000 -> O(N)

import sys
N = int(input())
numbers = [0 for i in range(-4000, 4001)]
total = 0
for _ in range(N):
    temp = int(sys.stdin.readline().strip())
    numbers[temp+4000] += 1
    total += temp

# 산술 평균 출력
print(round(total/N))

# 중앙값 출력 부분
mid_index = (N-1)//2+1
temp = 0

for i in range(len(numbers)):
    temp += numbers[i]
    if temp >= mid_index: # 처음 mid index 보다 값 넘으면 중앙값 이므로 for문 break
        print(i-4000)
        break

# 최빈값 출력 부분
frequent = max(numbers)
indexes = [i for i in range(len(numbers)) if numbers[i] == frequent]

if len(indexes) == 1:
    print(indexes[0]-4000)
else:
    print(indexes[1]-4000)

# 값의 범위 출력 부분
upper = 0
lower = 0
for i in range(8001):
    if numbers[i] != 0:
        lower = i-4000
        break

for i in range(8001):
    if numbers[8000-i] != 0:
        upper = 8000-i-4000
        break

print(upper-lower)
