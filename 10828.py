n = int(input())

stack = []
commends = []

for _ in range(n):
    commends.append(input().strip().split())

for commend in commends:
    if commend[0] == "push":
        stack.append(int(commend[1]))
    elif commend[0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])

    elif commend[0] == "size":
        print(len(stack))

    elif commend[0] == "empty":
        if not stack:
            print(1)
        else:
            print(0)

    elif commend[0] == "pop":
        if not stack:
            print(-1)
        else:
            top = stack.pop()
            print(top)