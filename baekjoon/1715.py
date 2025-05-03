import sys
import heapq

input = sys.stdin.readline

N = int(input())
array = [int(input()) for _ in range(N)]

if N == 1:
    print(0)
    exit()

if N == 2:
    print(sum(array))
    exit()

heapq.heapify(array)

answer = 0

while len(array) > 2:
    a = heapq.heappop(array)
    b = heapq.heappop(array)

    answer += (a+b)

    heapq.heappush(array, a+b)

if len(array) > 0:
    answer += sum(array)

print(answer)