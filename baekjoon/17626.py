# Silver 3
# O(N)
import math
from itertools import combinations_with_replacement

array = [0 for i in range(50001)]
array[0] = 1
squared_number_list = []
for i in range(1,50001):
    if math.sqrt(i).is_integer():
        array[i] = 1
        squared_number_list.append(i)
combs = list(combinations_with_replacement(squared_number_list, 2))
two_squares = []
for comb in combs:
    if sum(comb) <= 50000:
        if array[sum(comb)] == 0:
            array[sum(comb)] = 2
            two_squares.append(sum(comb))

for square in squared_number_list:
    for two_square in two_squares:
        if (square + two_square <= 50000) and array[square + two_square] == 0:
            array[square+two_square] = 3

n = int(input())
if array[n] == 0:
    print(4)
else:
    print(array[n])