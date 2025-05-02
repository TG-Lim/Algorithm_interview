from collections import deque
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # 양끝 처리. 1~N 까지 원본
        n = len(dominoes)
        extended_dominos = ['.', '.']
        extended_dominos.extend(dominoes)
        extended_dominos.extend(['.', '.'])

        # 2 ~ N+1 원래 거

        now = 0
        temp = []
        queue = deque([])

        for i, d in enumerate(extended_dominos):
            if d != '.' and 2 <= i <= n+1:
                queue.append((i, d, now))
        
        while queue:
            i, d, t = queue.popleft()
            if t > now: # 다른 시간이 나오면 바꾸기
                for prev_i, prev_d in temp:
                    extended_dominos[prev_i] = prev_d
                temp = [] # 바꾼 뒤 초기화
                now = t

            if 2 <= i <= n+1:

                if d == 'R' and extended_dominos[i+1] == '.' and extended_dominos[i+2] != 'L':
                    queue.append((i+1, 'R', t+1))
                    temp.append((i+1, 'R'))

                elif d == 'L' and extended_dominos[i-1] == '.' and extended_dominos[i-2] != 'R':
                    queue.append((i-1, 'L', t+1))
                    temp.append((i-1, 'L'))

        for i, d in temp:
            extended_dominos[i] = d

        return ''.join(extended_dominos[2:-2])


if __name__ == "__main__":
    s = Solution()
    print(s.pushDominoes("RR.L"))
    print(s.pushDominoes('......L...L'))
    print(s.pushDominoes(".L.R...LR..L.."))