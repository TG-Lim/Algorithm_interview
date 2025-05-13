class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = int(1e9) + 7
        cnt = [0] * 26  # a ~ z

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        for _ in range(t):
            new_cnt = [0] * 26
            for i in range(25):  # 'a' to 'y'
                new_cnt[i + 1] = cnt[i]
            # z → a + b
            new_cnt[0] += cnt[25]
            new_cnt[1] += cnt[25]
            cnt = new_cnt

        return sum(cnt) % mod

if __name__ == '__main__':
    cases = [
        ["abcyy", 2],
        ["azbk", 1],
    ]

    for case in cases:
        output = Solution().lengthAfterTransformations(case[0], case[1])
        print(output)