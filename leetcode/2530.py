from typing import List
import heapq
from math import ceil
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        q = []
        for n in nums:
            heapq.heappush(q, (-n, n))

        answer = 0

        for _ in range(k):
            _, num = heapq.heappop(q)
            answer += num
            next = ceil(num/3)
            heapq.heappush(q, (-next, next))

        return answer

if '__main__' == __name__:
    cases = [
        [[10,10,10,10,10], 5],
        [[1,10,3,3,3], 3]
    ]

    for case in cases:
        output = Solution().maxKelements(case[0], case[1])
        print(output)