# Gold 4
# 자료구조
import heapq
import sys
input = sys.stdin.readline
T = int(input())
result = []
for _ in range(T):
    k = int(input())
    max_q = []
    min_q = []
    cnt = {}
    for _ in range(k):
        c, n = input().strip().split()
        n = int(n)
        if c == 'I':
            heapq.heappush(min_q, n)
            heapq.heappush(max_q, -n)
            if n not in cnt:
                cnt[n] = 1
            else:
                cnt[n] += 1
        elif c == 'D':
            if n == 1:
                while max_q and cnt[-max_q[0]] == 0: # min 과의 동기화. 개수가 0인데 힙 안에 있으면 안됨
                    heapq.heappop(max_q)
                if max_q:
                    maximum = -heapq.heappop(max_q)
                    cnt[maximum] -= 1
            elif n == -1:
                while min_q and cnt[min_q[0]] == 0: # max 와의 동기화. 개수가 0인데 힙 안에 있으면 안됨
                    heapq.heappop(min_q)
                if min_q:
                    minimum = heapq.heappop(min_q)
                    cnt[minimum] -= 1
    while max_q and cnt[-max_q[0]] == 0:
        heapq.heappop(max_q)
    while min_q and cnt[min_q[0]] == 0:
        heapq.heappop(min_q)
    
    if not min_q or not max_q:
        result.append("EMPTY")
    else:
        result.append(f"{-max_q[0]} {min_q[0]}")

for res in result:
    print(res)