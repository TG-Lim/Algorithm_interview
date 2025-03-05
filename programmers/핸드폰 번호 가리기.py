def solution(phone_number):
    answer = '*'*(len(phone_number)-4)+phone_number[-4:]
    return answer

if __name__ == '__main__':
    cases = [
        "01033334444",
        "027778888"
    ]

    for case in cases:
        print(solution(case))