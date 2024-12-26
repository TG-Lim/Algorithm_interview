from collections import defaultdict
import string

def replace_punctuation_with_space(text):
    # Create a translation table that maps punctuation to spaces
    translator = str.maketrans({key: ' ' for key in string.punctuation})
    # Use the translation table to replace punctuation
    return text.translate(translator)

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        count = defaultdict(int)
        words = replace_punctuation_with_space(paragraph).lower().split()
        for word in words:
            count[word] += 1
        
        best = 0
        answer = ""
        for key, value in count.items():
            if key not in banned and value > best:
                best = value
                answer = key
        
        return answer
                
        

cases = [
    ["Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]],
    ["a.", []]
]

if __name__ == "__main__":
    for case in cases:
        solution = Solution()
        a = solution.mostCommonWord(paragraph=case[0], banned=case[1])
        print(a)