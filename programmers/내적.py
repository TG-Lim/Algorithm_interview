def solution(a, b):
    return sum([a[i]*b[i] for i in range(len(a))])

if __name__ == '__main__':
    cases = [
        ([1, 2, 3, 4], [-3, -1, 0, 2]),
        ([-1, 0, 1], [1, 0, -1]),
        ([1], [1]),
        ([1, 1], [1, 2])
    ]

    for case in cases:
        output = solution(case[0], case[1])
        print(output)