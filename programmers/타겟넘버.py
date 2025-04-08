def solution(numbers, target):
    answer = 0
    n = len(numbers)

    def backtrack(index, current_sum):
        nonlocal answer # 바깥 함수의 answer 변수를 사용

        # 모든 숫자를 다 사용했을 때 (재귀의 기저 사례)
        if index == n:
            if current_sum == target:
                answer += 1
            return # 재귀 종료

        # 현재 숫자를 더하는 경우
        backtrack(index + 1, current_sum + numbers[index])

        # 현재 숫자를 빼는 경우
        backtrack(index + 1, current_sum - numbers[index])

    # 백트래킹 시작 (첫 번째 숫자는 인덱스 0, 초기 합계는 0)
    backtrack(0, 0)

    return answer

if __name__ == '__main__':
    cases = [
        ([1, 1, 1, 1, 1], 3),
        ([4, 1, 2, 1], 4)
    ]

    for case in cases:
        print(solution(case[0], case[1]))