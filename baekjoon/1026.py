# Silver 4
# 정렬

N = int(input())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))

A.sort()
B.sort(reverse=True)

answer = 0
for i in range(N):
    answer += A[i]*B[i]

print(answer)