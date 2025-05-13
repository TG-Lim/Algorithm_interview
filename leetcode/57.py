from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        answer = []
        for start, end in intervals:
            if end < newInterval[0] or start > newInterval[1]: # 범위 밖
                answer.append([start, end])
                continue

            else:
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)
            
        answer.append(newInterval)
        answer.sort()

        return answer
    
if __name__ == '__main__':
    cases = [
        [[[1,3],[6,9]], [2,5]],
        [[[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]],
        [[], [2, 3]],
        [[[1, 3]], [5, 6]]
    ]

    for case in cases:
        output = Solution().insert(intervals=case[0],
                                   newInterval=case[1])
        print(output)