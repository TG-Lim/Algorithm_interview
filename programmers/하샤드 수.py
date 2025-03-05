def solution(x):
    a = sum(list(map(int, list(str(x)))))
    if x % a == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    cases = [10, 12, 11, 13, 6, 455]
    for case in cases:
        print(solution(case))