from collections import deque

n = int(input())
queue = deque([])
commends = []
for _ in range(n):
    commend = list(input().strip().split())
    commends.append(commend)

for commend in commends:
    if commend[0] == "push":
        queue.append(int(commend[1]))
    elif commend[0] == "pop":
        if not queue:
            print(-1)
        else:
            pop = queue.popleft()
            print(pop)
    elif commend[0] == "size":
        print(len(queue))
    elif commend[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif commend[0] == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif commend[0] == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])