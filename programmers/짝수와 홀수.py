def solution(num):
    if num == 0:
        return "Even"
    answer = "Even" if num % 2 == 0 else "Odd"
    return answer

if __name__ == '__main__':
    cases = [0, 1, 2, 3]
    for case in cases:
        answer = solution(case)
        print(answer)