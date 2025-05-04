from math import comb
class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        cnt = {}
        for domino in dominoes:
            domino.sort()
            domino_key = ''.join(str(d) for d in domino)
            if domino_key in cnt:
                cnt[domino_key] += 1
            else:
                cnt[domino_key] = 1

        answer = sum(comb(value, 2) for value in cnt.values() if value >= 2)
        return answer
if __name__ == '__main__':
    cases = [
        [[1, 2], [2, 1], [3, 4], [5, 6]],
        [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]
    ]

    for case in cases:
        output = Solution().numEquivDominoPairs(case)
        print(output)