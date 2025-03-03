def solution(x, n):
    answer = [(1+i)*x for i in range(n)]
    return answer

if __name__ == '__main__':
    cases = [(2, 5), (4, 3), (-4, 2)]
    for case in cases:
        answer = solution(case[0], case[1])
        print(answer)