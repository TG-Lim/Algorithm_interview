# Silver 1
A, B, C = map(int, input().strip().split())

answer = A%C
for i in range(B-1):
    temp = answer*A
    if temp < C:
        answer = temp
    else:
        answer = temp % C
print(answer)