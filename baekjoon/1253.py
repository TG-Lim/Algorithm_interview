from collections import defaultdict
from itertools import combinations

N = int(input())
array = list(map(int, input().strip().split()))

counter = defaultdict(int)

answer = 0

for a in array:
    counter[a] += 1

if 0 in counter:
    ##  0 처리
    # 0 + 0 = 0
    if counter[0] >= 3:
        answer += counter[0]
        counter[0] = 0

    # a + 0 = a
    for num in counter:
        if num != 0 and counter[num] >= 2:
            answer += counter[num]
            counter[num] = 0


combs = combinations(range(N), 2)

for i, j in combs:
    temp = array[i] + array[j]
    if temp in counter and array[i] != 0 and array[j] != 0:
        answer += counter[temp]
        counter[temp] = 0
    
print(answer)