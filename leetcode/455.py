class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()

        num_child = len(g)
        num_cookie = len(s)

        i = 0 # child index
        j = 0 # cookie index
        answer = 0

        while i < num_child and j < num_cookie:
            if g[i] <= s[j]:
                answer += 1
                i += 1
                j += 1

            else: # 쿠키가 작음
                j += 1

        return answer
        
if __name__ == "__main__":
    cases = [
        ([1, 2, 3], [1, 1], 1),
        ([1, 2], [1, 2, 3], 2),
        ([1], [1], 1),
        ([1], [], 0),
        ([5, 5, 5, 5, 5], [4, 4, 4, 4], 0)
    ]

    for case in cases:
        result = Solution().findContentChildren(case[0], case[1])
        print(f"result: {result} / answer: {case[2]}")