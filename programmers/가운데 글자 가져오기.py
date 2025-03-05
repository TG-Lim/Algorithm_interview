def solution(s):
    if len(s) % 2 == 1: # 홀수
        return s[len(s)//2]
    else: # 홀수
        return s[len(s)//2-1:len(s)//2+1]