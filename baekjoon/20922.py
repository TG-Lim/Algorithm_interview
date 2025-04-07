import sys
from collections import defaultdict

input = sys.stdin.readline

N, K = map(int, input().strip().split())
array = list(map(int, input().strip().split()))

start, end = 0, 0


cnt = defaultdict(int)
max_cnt = 1
cnt[array[start]] += 1
