roman_to_int = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900
}

for i in range(3):
    roman_to_int['I'*(i+1)] = i+1
    roman_to_int['X'*(i+1)] = 10*(i+1)
    roman_to_int['C'*(i+1)] = 100*(i+1)
    roman_to_int['M'*(i+1)] = 1000*(i+1)
    
roman_to_int['V'] = 5
roman_to_int['L'] = 50
roman_to_int['D'] = 500

class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        index = 0
        while index < len(s):
            for i in range(3, 0, -1):
                part = s[index:index+i]
                if part in roman_to_int:
                    answer += roman_to_int[part]
                    index = index + i
                    break
                else:
                    pass
        return answer
            
    
cases = [
    "III", "LVIII", "MCMXCIV", "I", "MMD"
]

if __name__ == "__main__":
    for case in cases:
        solution = Solution()
        print(solution.romanToInt(case))
