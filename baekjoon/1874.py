# Silver 2
# 1 <= N <= 100,000 -> O(NlogN)
import sys
from collections import deque
n = int(input())
array = deque([])
for _ in range(n):
    array.append(int(sys.stdin.readline().strip()))

stack = []
used = [False]*(n+1) # 사용 여부에 대한 점검 리스트
result = []
last = 0
while array:
    a = array.popleft()
    if stack and a == stack[-1]: # stack이 안 비어 있고, stack에 있는 경우
        result.append("-")
        stack.pop()
    else:
        if used[a]: # stack에 한번이라도 들어간 경우 -> 수열 만들 수 없음
            print("NO")
            exit()
        else:
            for i in range(last+1, a+1):
                stack.append(i)
                used[i] = True
                result.append("+")
            stack.pop()
            result.append("-")
            last = a
print('\n'.join(result))