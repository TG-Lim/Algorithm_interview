from collections import defaultdict
def solution():
    N = int(input())
    string = input().strip()
    length = len(string)
            
    start = 0
    distinct = 0
    answer = 0
    freq = defaultdict(int)  # 문자 빈도 추적
    
    for end in range(length):
        # end 문자 추가
        char_end = string[end]
        
        # 새로운 문자열 추가되었으므로 길이 증가
        if freq[char_end] == 0:
            distinct += 1
        freq[char_end] += 1
        
        # distinct > N이면 start 이동
        while distinct > N:
            char_start = string[start]
            freq[char_start] -= 1
            if freq[char_start] == 0:
                distinct -= 1
            start += 1
        
        # 유효한 부분 문자열 길이 갱신
        answer = max(answer, end - start + 1)
        
    print(answer)

solution()