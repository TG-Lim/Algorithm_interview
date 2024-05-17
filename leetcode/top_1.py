# https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 and n != 0:
            nums1 = []
            nums2 = nums2[:n]
            nums2.sort()
            nums1 = nums1 + nums2[:n]
            nums1.sort()
        elif m != 0 and n == 0:
            nums1 = nums1[:m]
            nums1.sort()
            nums2 = []
            
        elif m == 0 and n == 0:
            nums1 = []
            nums2 = []
        elif m != 0 and n != 0:
            nums1 = nums1[:m]
            nums2 = nums2[:n]
            print(nums2)
            nums1 = nums1 + nums2
            nums1.sort()
            nums2.sort()
            print(nums2)
            print(nums1)

s = Solution().merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)