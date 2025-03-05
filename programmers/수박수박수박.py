def solution(n):
    if n % 2 == 0: # 수박
        return "수박"*(n//2)
    else: # 수박수
        return "수박"*(n//2)+"수"

if __name__ == '__main__':
    cases = [1, 2, 3, 4]
    for case in cases:
        print(solution(case))