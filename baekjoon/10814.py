# Silver 5
# 1 <= N <= 100,000 -> O(N), std in, out

import sys
n = int(input())

array = []
for i in range(n):
    temp = list(sys.stdin.readline().strip().split())
    temp[0] = int(temp[0])
    temp.append(i)
    array.append(temp)

array.sort(key=lambda x: (x[0], x[2]))

for i in range(len(array)):
    age, name = array[i][0], array[i][1]
    if i < len(array)-1:
        temp = str(age)+' '+str(name)+'\n'
    else:
        temp = str(age)+' '+str(name)
    sys.stdout.write(temp)