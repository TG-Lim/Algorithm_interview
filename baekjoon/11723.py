# Silver 5
# 1 <= M <= 3,000,000 -> O(N)
import sys
M = int(input())
result = set()
for _ in range(M):
    inputs = list(sys.stdin.readline().rstrip().split())
    if inputs[0] == "add":
        result.add(int(inputs[1]))
    if inputs[0] == "remove":
        if int(inputs[1]) in result:
            result.remove(int(inputs[1]))
    if inputs[0] == "check":
        if int(inputs[1]) in result:
            print(1)
        else:
            print(0)
    if inputs[0] == "toggle":
        if int(inputs[1]) in result:
            result.remove(int(inputs[1]))
        else:
            result.add(int(inputs[1]))
    if inputs[0] == "all":
        result = set([i for i in range(1, 21)])
    if inputs[0] == "empty":
        result = set()