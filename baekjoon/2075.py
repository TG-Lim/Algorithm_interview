# Silver 2
import sys
input = sys.stdin.readline

N = int(input())
array = []
for _ in range(N):
    temp = list(map(int, input().split()))
    array.extend(temp)
    array.sort()
    array = array[-N:]
print(array[0])