def solution(n):
    element_list = list(map(int, list(str(n))))
    element_list.sort(reverse=True)

    answer = 0
    length = len(element_list)
    for i in range(length):
        answer += element_list[i]*(10**(length-1-i))

    return answer

if __name__ == '__main__':
    cases = [
        118372,
        352,
        5,
        77,
        162346,
        800
    ]

    for case in cases:
        print(solution(case))