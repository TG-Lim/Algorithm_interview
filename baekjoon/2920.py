import sys

array = list(map(int, sys.stdin.readline().strip().split()))

ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = [8, 7, 6, 5, 4, 3, 2, 1]

if array == ascending:
    print("ascending")
elif array == descending:
    print("descending")
else:
    print("mixed")