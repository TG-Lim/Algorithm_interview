def solution(num):
    cnt = 0
    if num == 1:
        return 0
    while cnt < 500:
        if num % 2 == 0:
            num /= 2
            cnt += 1
        else:
            num *= 3
            num += 1
            cnt += 1

        if num == 1:
            return cnt
    return -1

if __name__ == '__main__':
    print(solution(1))