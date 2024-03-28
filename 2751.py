# Silver 2
# 깡구현이나 데이터 개수가 커지면 표준입출력이 얼마나 좋은가를 보여주는 예시
import sys
N = int(input())

array = []

for _ in range(N):
    array.append(int(sys.stdin.readline().strip()))

array.sort()

for i in range(len(array)):
    if i < len(array)-1:
        sys.stdout.write(str(array[i]) + '\n')
    else:
        sys.stdout.write(str(array[i]))