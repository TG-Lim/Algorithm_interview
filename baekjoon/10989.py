# Bronze 1
import sys
N = int(input())
count = [0] * 10001

for _ in range(N):
    number = int(sys.stdin.readline().rstrip())
    count[number] += 1

for i in range(10001):
    if count[i] > 0:
        for _ in range(count[i]):
            sys.stdout.write(f"{i}\n")