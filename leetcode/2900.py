from typing import List
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        length = len(words)
        if length == 1:
            return words
        
        dp = [[0, 0] for _ in range(length)] # dp[i][j]: i번째 단어까지 고려했을 때 j 그룹으로 끝날 때 최대 길이
        parent = [None]*length

        for i in range(length):
            dp[i][groups[i]] = len(words[i])
        
        for i in range(1, length):
            group = groups[i]
            for j in range(i):
                if dp[i][group] < dp[j][1-group] + len(words[i]):
                    dp[i][group] = dp[j][1-group] + len(words[i])
                    parent[i] = j
        
        max_index = None
        for i in range(length):
            if max_index is None:
                max_index = i
                continue

            if max(dp[i]) > max(dp[max_index]):
                max_index = i

        result_index = []
        while max_index is not None:
            result_index.append(max_index)
            max_index = parent[max_index]
        
        result_index.reverse()
        
        return [words[r] for r in result_index]
        

if __name__ == '__main__':
    cases = [
        [["e","a","b"],[0, 0, 1]],
        [["a","b","c","d"], [1, 0, 1,1]],
        [['c'], [0]],
        [['d'], [1]],
    ]

    for case in cases:
        output = Solution().getLongestSubsequence(case[0], case[1])
        print(output)