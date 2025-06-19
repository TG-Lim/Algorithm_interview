from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        array = []
        for x, y in points:
            temp = [x, y, (x**2+y**2)**0.5]
            array.append(temp)
        
        array.sort(key=lambda x: x[-1])
        return [[x, y] for x, y, _ in array[:k]]