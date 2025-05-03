class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        n_to_str = {
            1: [''],
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
            0: ['']
        }

        if digits == '':
            return []

        digit_list = list(digits)
        result = []
        
        def backtracking(temp: list, index: int):
            if index == len(digit_list):
                result.append(''.join(temp))
                return
            
            for n in n_to_str[int(digit_list[index])]:
                temp.append(n)
                backtracking(temp, index+1)
                temp.pop() # 사용한 거 반환
        
        backtracking([], 0)
        return result


if __name__ == '__main__':
    cases = [
        '23', '', '2', '1', '0', '213'
    ]

    for case in cases:
        output = Solution().letterCombinations(case)
        print(output)