from collections import defaultdict
from typing import List
N = int(input()) # 1 ~ 10
words: List[str] = [input().strip() for _ in range(N)] # 단어길이 1 ~ 8

alphabets = defaultdict(int) # 각 단어마다 단어가 해당하는 자리수를 더해서 큰 순서대로 수 할당 예정

for word in words:
    for i in range(-1, -(len(word)+1), -1):
        alphabets[word[i]] += 10**(-(i+1))

values = sorted(list(alphabets.values()), reverse=True)
nums = list(range(9, -1, -1))[:len(values)]

print(sum(v*n for v, n in zip(values, nums)))