def solution(a, b):
    if a == b:
        return a

    bigger, smaller = max(a, b), min(a, b)
    return sum([i for i in range(smaller, bigger+1)])

if __name__ == '__main__':
    cases = [(3, 5), (3, 3), (5, 3), (-4, 3), (-5, -8)]
    for case in cases:
        output = solution(case[0], case[1])
        print(output)