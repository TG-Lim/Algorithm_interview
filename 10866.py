from collections import deque

n = int(input())
queue = deque([])
commends = []
for _ in range(n):
    commend = list(input().strip().split())
    commends.append(commend)

d = deque([])
for commend in commends:
    if commend[0] == 'push_back':
        d.append(int(commend[1]))
    elif commend[0] == 'push_front':
        d.appendleft(int(commend[1]))
    elif commend[0] == "pop_front":
        if not d:
            print(-1)
        else:
            p = d.popleft()
            print(p)
    elif commend[0] == 'pop_back':
        if not d:
            print(-1)
        else:
            p = d.pop()
            print(p)
    elif commend[0] == "size":
        print(len(d))
    elif commend[0] == "empty":
        if not d:
            print(1)
        else:
            print(0)

    elif commend[0] == 'front':
        if not d:
            print(-1)
        else:
            print(d[0])
    elif commend[0] == 'back':
        if not d:
            print(-1)
        else:
            print(d[-1])