# Silver 4
import sys
N = int(input())
array = []
for _ in range(N):
    array.append(int(sys.stdin.readline().rstrip()))
array.sort(reverse=True)
cnt = 1
answer = 0
for a in array:
    weight = a*cnt
    if weight >= answer:
        answer = weight
    cnt += 1

print(answer)