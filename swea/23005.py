from collections import deque
def solution():
    # 길이 100000 이므로 O(N) 혹은 O(NlogN) 복잡도로 풀기
    answers = []
    T = int(input())
    for _ in range(T):
        word = input().strip()
        length = len(word)

        if length == 1:
            answers.append(0)
            continue

        answer = 0
        queue = deque(word)

        while queue:
            
            if len(queue) == 1: # 하나 일때는 탈출시키기
                queue.pop()
                continue
                
            if queue[0] == queue[-1]: # 같음
                queue.pop()
                queue.popleft()
                continue

            else:
                if queue[0] == 'x':
                    queue.popleft()
                    answer += 1
                    continue

                elif queue[-1] == 'x':
                    queue.pop()
                    answer += 1
                    continue
                    
                else:
                    break

        if queue: # 회문 못만드는 경우
            answers.append(-1)
        else:
            answers.append(answer)

    print('\n'.join(str(answer) for answer in answers))


if __name__ == '__main__':
    solution()