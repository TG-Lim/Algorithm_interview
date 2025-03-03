def solution(n):
    n_to_str = list(str(n))
    return list(map(int, n_to_str[::-1]))

if __name__ == '__main__':
    cases = [12345, 234, 1000000000]
    for case in cases:
        output = solution(case)
        print(output)