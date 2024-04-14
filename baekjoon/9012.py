import sys
n = int(input())
strings = []
for _ in range(n):
    strings.append(sys.stdin.readline().strip())

for string in strings:
    temp = 0
    is_VPS = True
    for s in string:
        if s == "(":
            temp += 1
        else:
            temp -= 1
        if temp < 0:
            is_VPS = False
    if not is_VPS:
        print("NO")
    if is_VPS and temp == 0:
        print("YES")
    if is_VPS and temp != 0:
        print("NO")