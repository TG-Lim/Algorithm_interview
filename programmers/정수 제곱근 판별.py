def solution(n):
    sqrt = n**0.5
    if int(sqrt) == sqrt:
        return int((sqrt+1)**2)
    else:
        return -1

if __name__ == '__main__':
    cases = [121, 3, 144, 34]
    for case in cases:
        print(solution(case))