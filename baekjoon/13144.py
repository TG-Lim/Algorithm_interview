N = int(input())
array = list(map(int, input().split()))

answer = 0
start = 0
seen = set()

for end in range(N):
    while array[end] in seen:
        seen.remove(array[start])
        start += 1
    seen.add(array[end])
    answer += (end - start + 1)

print(answer)