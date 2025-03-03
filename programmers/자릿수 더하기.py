def solution(n):
    n_to_str = list(str(n))
    answer = sum([int(s) for s in n_to_str])
    return answer

if __name__ == "__main__":
    cases = [123, 987, 100, 1, 123490]
    for case in cases:
        output = solution(case)
        print(output)