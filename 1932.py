# Silver 1, Dynamic Programming
# N<= 500 -> O(N^3) okay
import sys
n = int(sys.stdin.readline())
triangle = []

for i in range(n):
    temp = list(map(int, sys.stdin.readline().strip().split(' ')))
    triangle.append(temp)

scores = [[0 for _ in range(i)] for i in range(1,n+1)]

scores[0][0] += triangle[0][0]

for i in range(1,n):
    scores[i][0] = scores[i-1][0] + triangle[i][0]
    scores[i][-1] += scores[i-1][-1] + triangle[i][-1]

    for j in range(1,i):
        scores[i][j] = max(scores[i-1][j-1] + triangle[i][j], scores[i-1][j] + triangle[i][j])

print(max(scores[-1]))