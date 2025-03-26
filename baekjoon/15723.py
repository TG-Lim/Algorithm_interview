import sys
input = sys.stdin.readline

n = int(input())
bool_array = [[False]*(26) for _ in range(26)]

standard = ord('a')

for _ in range(n):
    inputs = input().strip().split()
    bool_array[ord(inputs[0])-standard][ord(inputs[-1])-standard] = True

for i in range(26):
    bool_array[i][i] = True

for k in range(26):
    for i in range(26):
        for j in range(26):
            bool_array[i][j] = bool_array[i][j] or (bool_array[i][k] and bool_array[k][j])

m = int(input())
answer = []
for _ in range(m):
    inputs = input().strip().split()
    p, q = ord(inputs[0])-standard, ord(inputs[-1])-standard
    if bool_array[p][q]:
        answer.append('T')
    else:
        answer.append('F')

print('\n'.join(answer))