def solution(s):
    if s[0] == '-':
        return -int(s[1:])
    else:
        return int(s)

cases = ["-1234", "1234"]
if __name__ == '__main__':
    for case in cases:
        output = solution(case)
        print(output)