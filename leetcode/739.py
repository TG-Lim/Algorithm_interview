from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
        
        return answer

if __name__ == '__main__':
    cases = [
        [73,74,75,71,69,72,76,73],
        [30,40,50,60],
        [30,60,90]
    ]

    for case in cases:
        output = Solution().dailyTemperatures(case)
        print(output)