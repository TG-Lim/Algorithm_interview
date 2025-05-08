from typing import List
from collections import deque
class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.height = height
        self.width = width
        self.array = [[0]*width for _ in range(height)]
        self.food = food
        self.food_index = 0
        self.is_body = [[False]*width for _ in range(height)]
        self.is_body[0][0] = True
        self.body = deque([(0, 0)])
    
    def get_food(self):
        food =  self.food[self.food_index]
        return food[0], food[1]

    def move(self, direction: str) -> int:
        if direction == 'R':
            dr, dc = 0, 1
        elif direction == 'U':
            dr, dc = -1, 0
        elif direction == 'L':
            dr, dc = 0, -1
        elif direction == 'D':
            dr, dc = 1, 0
        
        nr, nc = self.body[-1][0] + dr, self.body[-1][1] + dc
        if nr == -1 or nr == self.height or nc == -1 or nc == self.width: # 게임 탈락
            return -1
        
        fr, fc = self.get_food()
        if nr == fr and nc == fc: # 음식먹음 -> 몸길이 늘어남
            self.body.append((nr, nc))
            self.is_body[nr][nc] = True


if __name__ == '__main__':
    obj = SnakeGame(3, 2, [[1,2],[0,1]])
    patterns = [["R"],["D"],["R"],["U"],["L"],["U"]]
    for pattern in patterns:
        score = obj.move(pattern[0])
        print(score)