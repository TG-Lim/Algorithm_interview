# Silver 5
# 1 <= N <= 100,000 -> 빠른 입출력 사용 및 O(N)

import sys
N = int(sys.stdin.readline())
array = []
for _ in range(N):
    position = list(map(int, sys.stdin.readline().strip().split()))
    array.append(position)

array.sort(key=lambda x: (x[0], x[1]))

for i in range(len(array)):
    x, y = array[i][0], array[i][1]
    if i < len(array)-1:
        temp = str(x)+' '+str(y)+'\n'
    else:
        temp = str(x)+' '+str(y)
    sys.stdout.write(temp)