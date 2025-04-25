class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        
        result = [[]]
        length = len(nums)

        def backtracking(start: int, arr: list, r: int): # start: 시작 인덱스, arr: 저장 배열, r: 추출할 개수
            if len(arr) == r:
                result.append(arr[:])
                return
            
            for i in range(start, length):
                arr.append(nums[i])
                backtracking(i+1, arr, r)
                arr.pop()
        
        for r in range(1, length+1):
            backtracking(0, [], r)

        return result

if __name__ == '__main__':
    cases = [
        [1, 2, 3],
        [0],
        [1, 2, 3, 4, 5]
    ]
    for case in cases:
        output = Solution().subsets(case)
        print(output)