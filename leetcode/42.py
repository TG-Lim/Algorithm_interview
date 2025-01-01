class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)

            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume     


if "__main__" == __name__:
    cases = [
        [0,1,0,2,1,0,1,3,2,1,2,1],
        [4,2,0,3,2,5]
    ]

    for case in cases:
        solution = Solution()
        answer = solution.trap(height=case)
        print(answer)


"""
물이 찰 때 왼쪽 방향 제일 높은 곳과 오른쪽 방향 제일 높은 곳 중 더 낮은 곳을 기준으로 찬다.
즉 왼쪽 방향 제일 높은 곳의 높이가 3인 경우 오른쪽 방향 제일 높은 곳의 높이는 10 이든 100 이든 상관이 없음
계속 꾸준히 왼쪽 방향 제일 높은 곳 높이와 오른쪽 방향 제일 높은 곳 높이를 업데이트 하는 방향으로 살펴봐야 함
Pseudo Code
Function trap(height):
    Check if height is non-value list
    if len(height) is 0:
        return 0

    Initialize volume, left and right index
    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        Update maximum heights from both ends
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)

        Trapping water based on lower max
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    
    return volume
"""