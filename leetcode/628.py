class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        pos_index = None

        for i in range(len(nums)):
            if nums[i] >= 0:
                pos_index = i
                break

        if pos_index is None: # nums 에 양수 없음 -> 뒤에 숫자 세 개
            answer = nums[-1]*nums[-2]*nums[-3]
            return answer

        answer = max(nums[0]*nums[1])
        

if __name__ == '__main__':
    cases = [
        ([1, 2, 3], 6),
        ([1, 2, 3, 4], 24),
        ([-1, -2, -3], -6)
    ]

    for case in cases:
        output = Solution().maximumProduct(case[0])
        print(f"Output: {output} / Expectation: {case[1]}")