class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = []
        p = 1
        for i in range(0, len(nums)):
            answer.append(p)
            p *= nums[i]

        p = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= p
            p *= nums[i]

        return answer        


if "__main__" == __name__:
    cases = [
        [1, 2, 3, 4],
        [-1, 1, 0, -3, 3]
    ]

    for case in cases:
        solution = Solution()
        print(solution.productExceptSelf(nums=case))