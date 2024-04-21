# Silver 3
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))
problems = []
for _ in range(M):
    problem = list(map(int, sys.stdin.readline().rstrip().split()))
    problems.append(problem)

sum_array = [0 for _ in range(N+1)]
for i in range(N):
    sum_array[i+1] = sum_array[i]+array[i]

result = []
for problem in problems:
    start, end = problem[0], problem[1]
    answer = sum_array[end]-sum_array[start-1]
    result.append(answer)

sys.stdout.write('\n'.join(str(n) for n in result))