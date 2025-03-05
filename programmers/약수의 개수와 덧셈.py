def get_yaksu(number):
    cnt = 0
    n_sqrt = number ** 0.5

    for n in range(1, int(n_sqrt)+1):
        if n < n_sqrt and number % n == 0:
            cnt += 2

        elif n == int(n_sqrt) and number % n == 0:
            cnt += 1 # 제곱수

    return cnt

def solution(left, right):
    answer = 0
    for number in range(left, right+1):
        cnt = get_yaksu(number)
        if cnt % 2 == 0:
            answer += number
        else:
            answer -= number

    return answer

if __name__ == '__main__':
    cases = [1, 2, 3, 4, 8, 9]
    for case in cases:
        print(get_yaksu(case))