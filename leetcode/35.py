class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums)-1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1

        return start



if __name__ == '__main__':
    cases = [
        ([1, 3, 5, 6], 5),
        ([1, 3, 5, 6], 2),
        ([1, 3, 5, 6], 7)
    ]

    for case in cases:
        output = Solution().searchInsert(case[0], case[1])
        print(output)