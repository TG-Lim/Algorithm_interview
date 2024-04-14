import sys

N = int(sys.stdin.readline().strip())
array = []
for _ in range(N):
    array.append(sys.stdin.readline().strip())

array = list(set(array))
array.sort(key=lambda x: (len(x), x))

for a in array:
    print(a)