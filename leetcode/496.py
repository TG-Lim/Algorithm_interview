"""
어떤 배열에서 특정 요소 x의 다음 큰 요소란 x의 오른쪽에 위치한 첫 번째 더 큰 요소를 의미합니다.
두 개의 서로 다른 0-인덱스 정수 배열 nums1과 nums2가 주어지며, nums1은 nums2의 부분집합입니다.
각 0 <= i < nums1.length에 대해, nums1[i] == nums2[j]인 인덱스 j를 찾고, nums2[j]의 다음 큰 요소를 nums2에서 결정합니다. 만약 다음 큰 요소가 존재하지 않으면 해당 값은 -1이 됩니다.
이러한 조건에 따라 nums1.length 크기의 배열 ans를 반환해야 하며, ans[i]는 위에서 설명한 다음 큰 요소입니다.
"""

from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_dict = {nums2[i]: i for i in range(len(nums2))} # key: nums2 숫자 / value: 인덱스

        answer = []

        for num in nums1:
            index = num_dict[num] # num1 의 원소의 num2 에서의 인덱스

            part_array = nums2[index+1:]
            
            inserted = False
            for part in part_array:
                if part > num: # 이 숫자보다 큼
                    answer.append(part)
                    inserted = True
                    break

            if not inserted:
                answer.append(-1)

        return answer

if __name__ == '__main__':
    cases = [
        [[4, 1, 2], [1, 3, 4, 2]],
        [[2, 4], [1, 2, 3, 4]]
    ]

    for case in cases:
        output = Solution().nextGreaterElement(case[0], case[1])
        print(output)