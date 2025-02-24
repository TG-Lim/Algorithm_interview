import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            
            x, y = max(first, second), min(first, second) # 가벼운 돌, 큰 돌순
            
            if x != y:
                heapq.heappush(heap, y-x)
        
        if len(heap) == 0:
            return 0
        else:
            return -heap[0]    
    
if __name__ == "__main__":
    cases = [
        ([2, 7, 4, 1, 8, 1], 1),
        ([1], 1),
        ([1, 1], 0)
    ]
    
    for case in cases:
        result = Solution().lastStoneWeight(case[0])
        print(f"result: {result} / answer: {case[1]}")