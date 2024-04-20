# Silver 4
import sys
N, M = map(int, input().split())
dictionary = {}
dictionary_poke = {}
for i in range(1,N+1):
    poke = sys.stdin.readline().rstrip()
    dictionary[i] = poke
    dictionary_poke[poke] = i

for _ in range(M):
    problem = sys.stdin.readline().rstrip()
    if problem.isdigit():
        sys.stdout.write(dictionary[int(problem)]+'\n')
    else:
        sys.stdout.write(str(dictionary_poke[problem])+'\n')