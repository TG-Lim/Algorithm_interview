from typing import List

class Solution:
    def matmul(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        mod = int(1e9) + 7
        size = 26
        C = [[0] * size for _ in range(size)]
        for i in range(size):
            for k in range(size):
                if A[i][k] == 0:
                    continue
                for j in range(size):
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod
        return C

    def matrix_power(self, matrix: List[List[int]], t: int) -> List[List[int]]:
        size = 26
        res = [[int(i == j) for j in range(size)] for i in range(size)]  # 단위 행렬
        while t:
            if t % 2 == 1:
                res = self.matmul(res, matrix)
            matrix = self.matmul(matrix, matrix)
            t //= 2
        return res

    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        mod = int(1e9) + 7
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # 전이 행렬 생성: T[new][old] = 1
        matrix = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for j in range(1, nums[i] + 1):
                new_char = (i + j) % 26
                matrix[new_char][i] = 1  # 핵심 수정: old → new 전이

        # 행렬 거듭제곱
        Transform = self.matrix_power(matrix, t)

        # 최종 상태 계산: result = Transform × count
        final_count = [0] * 26
        for i in range(26):
            for j in range(26):
                final_count[i] = (final_count[i] + Transform[i][j] * count[j]) % mod

        return sum(final_count) % mod


if __name__ == '__main__':
    cases = [
        ["abcyy", 2, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]],
        ["azbk", 1, [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]
    ]

    for case in cases:
        output = Solution().lengthAfterTransformations(case[0], case[1], case[2])
        print(output)
