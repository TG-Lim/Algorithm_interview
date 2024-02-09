# Silver 3 DP
import sys
fibonacci = [[0, 0] for _ in range(41)]
# 0
fibonacci[0][0] = 1
fibonacci[0][1] = 0
# 1
fibonacci[1][0] = 0
fibonacci[1][1] = 1

for i in range(2, 41):
    fibonacci[i][0] = fibonacci[i-1][0] + fibonacci[i-2][0]
    fibonacci[i][1] = fibonacci[i-1][1] + fibonacci[i-2][1]

n = int(sys.stdin.readline())
numbers = []
for _ in range(n):
    number = int(sys.stdin.readline())
    numbers.append(number)

for number in numbers:
    print(fibonacci[number][0], fibonacci[number][1])