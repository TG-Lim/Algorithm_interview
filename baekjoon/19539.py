N = int(input())
array = list(map(int, input().strip().split()))

if sum(array) % 3 != 0: # 만족 안되는 경우
    print('NO')
    exit()

M = sum(h//2 for h in array)
K = sum(array) // 3

if M >= K:
    print('YES')
else:
    print('NO')
exit()