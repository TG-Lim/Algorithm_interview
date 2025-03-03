def solution(n):
    numbers = [i for i in range(1, n+1)]
    checked = [False]*(n+1)
    factors = set()

    for number in numbers:
        if checked[number] == True:
            continue

        if n % number == 0: # 약수인 경우
            checked[number] = True
            checked[n // number] = True

            factors.add(number)
            factors.add(n // number)
    return sum(factors)

cases = [12, 5, 1, 2, 3, 9]

if __name__ == '__main__':
    for case in cases:
        answer = solution(case)
        print(answer)