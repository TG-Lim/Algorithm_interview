while True:
    array = list(map(int, input().split()))
    if sum(array) == 0:
        exit()
    array.sort()
    array_square = [a**2 for a in array]
    if array_square[2] == array_square[0] + array_square[1]:
        print("right")
    else:
        print("wrong")