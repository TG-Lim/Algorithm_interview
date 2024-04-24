# Silver 2
# 1<= N <= 1,000,000 -> O(NlogN)
# 메모리 크기 <= 512MB
import sys
N = int(input())
array = list(map(int, sys.stdin.readline().rstrip().split()))
unique_array = sorted(list(set(array)))
transform = {}

for i in range(len(unique_array)):
    transform[unique_array[i]] = i

result = []
for a in array:
    result.append(transform[a])

print(' '.join(str(t) for t in result))

# # 1,000,000개의 key와 value를 가진 dictionary 생성
# large_dict = {i: i for i in range(1000000)}
#
# # dictionary의 메모리 사용량 확인
# dict_memory_usage = sys.getsizeof(large_dict)
#
# # 각 key와 value의 메모리 사용량을 추가로 계산
# total_memory = dict_memory_usage + sum(sys.getsizeof(key) + sys.getsizeof(value) for key, value in large_dict.items())
#
# print(total_memory)