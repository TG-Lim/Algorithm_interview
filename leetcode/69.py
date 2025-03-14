class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        start = 1
        end = x

        while start <= end:
            mid = (start + end) // 2
            if mid**2 == x:
                return mid

            elif mid**2 < x:
                start = mid+1

            elif mid**2 > x:
                end = mid-1

        return end
if __name__ == '__main__':
    cases = [1, 2, 4, 8, 9, 16, 23, 74, int(1e9)]
    for case in cases:
        output = Solution().mySqrt(case)
        print(output)