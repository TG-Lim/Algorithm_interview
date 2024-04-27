# Silver 3
import sys
N = int(input())
M = int(input())
S = sys.stdin.readline().rstrip()
P_N = "".join(["I" if i % 2 == 0 else "O" for i in range(2*N+1)])
length = 2*N+1
start = 0
end = 2*N+1
cnt = 0
iscorrect = False
while end <= M:
    if iscorrect:
        temp = S[end:end+2]
        if temp == "OI":
            cnt += 1
            end += 2
        else:
            iscorrect = False
            start = end
            end = start+length
    else:
        temp = S[start:end]
        if temp == P_N:
            iscorrect = True
            cnt += 1
        else:
            start += 1
            end += 1
print(cnt)