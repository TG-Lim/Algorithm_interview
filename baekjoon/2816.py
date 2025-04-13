N = int(input())
array = [input().strip() for _ in range(N)]
loc = 0

array[1], array[2] = array[2], array[1]
print(array)