import sys

array = list(map(int, sys.stdin.readline().strip().split()))

array_square = [t**2 for t in array]
print(sum(array_square)%10)