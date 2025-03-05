def solution(s):
    cnt = {
        'p': 0,
        'y': 0
    }
    s = s.lower()
    for alphabet in s:
        if alphabet in cnt:
            cnt[alphabet] += 1

    if cnt['p'] == cnt['y']:
        return True
    else:
        return False

if __name__ == "__main__":
    cases = [
        "pPoooyY",
        "Pyy",
        'abc'
    ]

    for case in cases:
        print(solution(case))