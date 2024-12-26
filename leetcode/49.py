from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for string in strs:
            sorted_word = sorted(string)
            anagrams[tuple(sorted_word)].append(string)
        
        return [value for value in anagrams.values()]

if __name__ == '__main__':
    cases = [
        ["eat","tea","tan","ate","nat","bat"],
        [""],
        ["a"]
    ]
    
    for case in cases:
        solution = Solution()
        answer = solution.groupAnagrams(strs=case)
        print(answer)
