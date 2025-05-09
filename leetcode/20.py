class Solution:
    def isValid(self, s: str) -> bool:
        pair_braket = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for string in s:
            if string not in pair_braket: # 왼쪽 방향 넣기
                stack.append(string)
            else:
                if stack and stack[-1] == pair_braket[string]: # 짝 지을 수 있음
                    stack.pop()
                else:
                    return False
        
        return not stack
    
if __name__ == '__main__':
    cases = [
        ')',
        '([])',
        '([]})'
    ]

    for case in cases:
        output = Solution().isValid(case)
        print(output)