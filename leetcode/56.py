from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        now_start = None
        now_end = None
        answer = []
        for start, end in intervals:
            if now_start is None and now_end is None:
                now_start = start
                now_end = end
                continue

            if now_end < start: # 안겹침
                answer.append([now_start, now_end])
                now_start, now_end = start, end
                continue

            else: # 겹침
                now_start = min(now_start, start)
                now_end = max(now_end, end)
        
        if len(answer) == 0 or answer[-1][1] != now_end: # 최종 구간 안넣었으면
            answer.append([now_start, now_end]) # 최종 구간 넣기
        return answer

if __name__ == '__main__':
    cases = [
        [[1,3],[2,6],[8,10],[15,18]],
        [[1,4],[4,5]],
        [[1,4],[0,0]],
        [[1,4]]
    ]

    for case in cases:
        output = Solution().merge(case)
        print(output)