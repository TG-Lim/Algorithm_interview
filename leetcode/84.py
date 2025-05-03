class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []  # 저장할 것은 index
        max_area = 0
        heights.append(0)  # 마지막 처리용 sentinel

        for i, h in enumerate(heights):
            # 높이가 떨어지는 순간 계산
            # 없는 경우 그냥 패스
            # 있는 경우 stack 에서 꺼내가면서 체크
            # 조건 만족하는 경우 바로 직사각형 만듦
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                # 스택이 비면 가로 길이는 i
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            # 새로 넣어가면서 가로 누적
            stack.append(i)
        
        heights.pop()  # sentinel 제거
        return max_area



if __name__ == '__main__':
    cases = [
        [2,1,5,6,2,3],
        [2,4]
    ]

    for case in cases:
        output = Solution().largestRectangleArea(case)
        print(output)