def solution(name):
    n = len(name)
    # 각 문자를 변경하는 최소 횟수 합
    up_down = sum(min(ord(char) - ord('A'), 26 - (ord(char) - ord('A'))) for char in name)
    
    # 최소 좌우 이동 횟수를 찾기
    min_move = n - 1  # 기본적으로 모든 글자를 오른쪽으로만 이동한다고 가정
    
    for i in range(n):
        next_i = i + 1
        # 다음 'A'가 아닌 위치를 찾음
        while next_i < n and name[next_i] == 'A':
            next_i += 1
        # i까지 오른쪽으로 간 후, 뒤로 돌아가는 경우
        distance = 2 * i + n - next_i
        min_move = min(min_move, distance)
        # i까지 왼쪽으로 간 후, 다시 오른쪽으로 가는 경우
        distance = i + 2 * (n - next_i)
        min_move = min(min_move, distance)
    
    return up_down + min_move