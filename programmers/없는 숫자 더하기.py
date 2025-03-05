def solution(numbers):
    base = set(range(10))
    numbers = set(numbers)

    delta = list(base - numbers)
    answer = sum(delta)
    return answer