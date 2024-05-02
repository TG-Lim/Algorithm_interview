# Silver 3
# DP
array = [0 for _ in range(101)]
array[1] = 1
array[2] = 1
array[3] = 1
array[4] = 2
array[5] = 2
for i in range(6, 101):
    array[i] = array[i-1] + array[i-5]

N = int(input())
test_case = []
for _ in range(N):
    test = int(input())
    test_case.append(test)
for test in test_case:
    print(array[test])