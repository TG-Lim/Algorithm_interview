from collections import deque
from typing import List

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        """
        작업 난이도(tasks)와 작업자 강도(workers)가 주어질 때,
        최대 몇 개의 작업을 할당할 수 있는지 반환합니다.
        - 알약(pill)을 사용하지 않으면 worker >= task 필요
        - 알약 사용 시 worker + strength >= task 필요
        """
        # 작업과 작업자를 오름차순으로 정렬
        tasks.sort()
        workers.sort()

        def can_assign(k: int) -> bool:
            """
            가장 쉬운 k개의 작업을 k명의 가장 강한 작업자에게 할당 가능한지 확인합니다.
            """
            task_queue = deque()
            pills_left = pills
            task_ptr = 0

            # 가장 강한 k명의 작업자를 순회
            for w in workers[-k:]:
                # 현재 작업자가 알약 사용 시 처리 가능한 작업들을 큐에 추가
                while task_ptr < k and tasks[task_ptr] <= w + strength:
                    task_queue.append(tasks[task_ptr])
                    task_ptr += 1

                # 할당할 작업이 없다면 실패
                if not task_queue:
                    return False

                # 알약 없이 처리 가능한 가장 쉬운 작업을 먼저 할당
                if task_queue[0] <= w:
                    task_queue.popleft()
                else:
                    # 알약이 남아있지 않으면 실패
                    if pills_left == 0:
                        return False
                    # 알약 사용 후 가장 어려운 작업을 할당
                    pills_left -= 1
                    task_queue.pop()

            return True

        # 이분 탐색으로 최대 할당 개수 탐색
        left, right = 0, min(len(tasks), len(workers))
        while left < right:
            mid = (left + right + 1) // 2
            if can_assign(mid):
                left = mid
            else:
                right = mid - 1
        
        return left

if __name__ == '__main__':
    cases = [
        ([3,2,1], [0,3,3], 1, 1), # 3
        ([5,4], [0,0,0], 1, 5), # 1
        ([10,15,30], [0,10,10,10,10], 3, 10), # 2
        ([5, 9, 8, 5, 9], [1, 6, 4, 2, 6], 1, 5) # 3
    ]

    for case in cases:
        output = Solution().maxTaskAssign(case[0], case[1], case[2], case[3])
        print(output)