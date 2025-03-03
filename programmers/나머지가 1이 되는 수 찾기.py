def solution(n):
    # 자기 자신을 뺀 수 중 1이 아닌 약수중에 제일 큰 수
    n -= 1
    for x in range(2, n+1):
        if n % x == 0:
            return x

if __name__ == '__main__':
    cases = [10, 12, 37] # 3, 11, 3
    for case in cases:
        output = solution(case)
        print(output)