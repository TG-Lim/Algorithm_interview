import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().strip().split()))
array.sort()

M = int(input())
array2 = list(map(int, input().strip().split()))

def find_location(num):
    start = 0
    end = len(array)-1

    while start <= end:
        mid = int((start+end)/2)
        if array[mid] == num:
            return 1

        elif array[mid] < num: # 값이 작으므로 start 당겨줌
            start = mid + 1

        elif array[mid] > num:
            end = mid - 1

    return 0

for a in array2:
    print(find_location(a))