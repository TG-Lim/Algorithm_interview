class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        min_number = min(nums)
        if min_number < k: # k 보다 밑에 값이 있는 경우 바꿀 수 없음
            return -1
        
        cnt = 0
        
        nums.sort(reverse=True)
        
        valid_index = 0
        valid_number = nums[valid_index]
        
        for i in range(len(nums)):
            n = nums[i]
            if n < valid_number: # 새로운 valid number 등장 
                valid_index = i
                valid_number = n
                cnt += 1
                     
        if valid_number == k:
            return cnt
        else:
            return cnt+1
    

# nums k answer
cases = [
    [[5, 2, 5, 4, 5],2, 2],
    [[2, 1, 2], 2, -1],
    [[9, 7, 5, 3], 1, 4],
    [[1, 2], 1, 1],
    [[7], 7, 0],
    [[7], 8, -1]
]

if __name__ == '__main__':
    for case in cases:
        solution = Solution()
        answer = solution.minOperations(nums=case[0], k=case[1])
        print(f"solve: {answer} / answer: {case[2]}")