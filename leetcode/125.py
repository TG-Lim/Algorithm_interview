from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
            
        return True
    
cases = [
    "A man, a plan, a canal: Panama",
    "race a car",
    ""
]

if __name__ == "__main__":
    for case in cases:
        solution = Solution()
        print(solution.isPalindrome(case))