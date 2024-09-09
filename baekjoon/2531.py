# Silver 1
# Two Pointer
import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
array = []
for _ in range(N):
    array.append(int(input()))

start_index = 0
end_index = start_index + k
answer = 0
temp = array[start_index:end_index]
while True:
    if start_index >= N:
        break
    sushi_type = set(temp)
    if c in sushi_type:
        answer = max(answer, len(sushi_type))
    else:
        answer = max(answer, len(sushi_type)+1)

    start_index += 1
    end_index = start_index + k
    if end_index >= N:
        temp = array[start_index:N]
        temp.extend(array[0:(end_index-N)])

    else:
        temp = array[start_index:end_index]


print(answer)