# Silver 3 DP

array = [0 for i in range(1001)]
array[1] = 1
array[2] = 3

for i in range(3,1001):
    array[i] = array[i-1] + 2*array[i-2]
n = int(input())
print(array[n] % 10007)