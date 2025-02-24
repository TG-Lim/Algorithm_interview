import heapq

class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        heap = [(-num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)
        
        temp = []
        for _ in range(k):
            temp.append(heapq.heappop(heap))
            
        
        temp.sort(key=lambda x: x[1])
        return [-num for num, _ in temp]
    
if __name__ == "__main__":
    cases = [
        ([2, 1, 3, 3], 2, [3, 3]),
        ([-1, -2, 3, 4], 3, [-1, 3, 4]),
        ([3, 4, 3, 3], 2, [3, 4]),
        ([1], 1, [1])
    ]
    
    for case in cases:
        result = Solution().maxSubsequence(case[0], case[1])
        print(f"result: {result} / answer: {case[2]}")