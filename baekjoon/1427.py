# Silver 5
array = list(map(int, list(input().strip())))
array.sort(reverse=True)

print(''.join(str(s) for s in array))