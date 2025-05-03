class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        answer = int(1e6)
        length = len(tops)
        for i in range(1, 7): # 1~6
            temp_tops = tops[:]
            temp_bottoms = bottoms[:]
            temp_cnt = 0
            # tops 부터
            for j in range(length):
                if temp_tops[j] != i:
                    temp_tops[j], temp_bottoms[j] = temp_bottoms[j], temp_tops[j]
                    temp_cnt += 1
            
            if all(t == i for t in temp_tops):
                answer = min(answer, temp_cnt)
            
            # bottoms
            temp_tops = tops[:]
            temp_bottoms = bottoms[:]
            temp_cnt = 0

            for j in range(length):
                if temp_bottoms[j] != i:
                    temp_tops[j], temp_bottoms[j] = temp_bottoms[j], temp_tops[j]
                    temp_cnt += 1
            
            if all(t == i for t in temp_bottoms):
                answer = min(answer, temp_cnt)
        
        if answer != int(1e6):
            return answer
        else:
            return -1

if __name__ == '__main__':
    cases = [
        ([2,1,2,4,2,2], [5,2,6,2,3,2]), # 2
        ([3,5,1,2,3], [3,6,3,3,4]), # -1
        ([1, 1], [3, 2]), # 0
    ]

    for case in cases:
        output = Solution().minDominoRotations(case[0], case[1])
        print(output)