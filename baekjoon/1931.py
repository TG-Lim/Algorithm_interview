# Silver 1
# 1<= N <= 100,000 -> O(NlogN)
import sys
N = int(input())
array = []
for _ in range(N):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    # temp.append(temp[1]-temp[0])
    array.append(temp)
array.sort(key=lambda x: (x[1], x[0]))
cnt = 1
end_time = array[0][1]
for i in range(1,N):
    if array[i][0] >= end_time:
        cnt += 1
        end_time = array[i][1]

print(cnt)