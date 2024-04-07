# Silver 5 구현
N = int(input())
cnt = 0
number = 666

while True:
    if '666' in str(number):
        cnt += 1
    if cnt == N:
        print(number)
        exit()
    number += 1