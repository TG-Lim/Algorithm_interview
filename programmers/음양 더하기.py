def solution(absolutes, signs):
    answer = 0
    length = len(absolutes)
    for i in range(length):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer

if __name__ == '__main__':
    cases = [
        ([4, 7, 12], [True, False, True]),
        ([1,2, 3], [False, False, True])
    ]

    for case in cases:
        print(solution(case[0], case[1]))