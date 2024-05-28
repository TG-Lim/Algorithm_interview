from itertools import combinations
import sys
input = sys.stdin.readline
arraies = []
while True:
    array = list(map(int, input().strip().split()))
    if array[0] == 0:
        break
    arraies.append(array)
result = []
for array in arraies:
    lotto = list(combinations(array[1:], 6))
    for l in lotto:
        list_l = list(l)
        list_l.append('\n')
        sys.stdout.write(' '.join(str(l2) for l2 in list_l))
    print('')