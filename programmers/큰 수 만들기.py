def solution(number, k):
    stack = []
    for n in number:
        while k > 0 and stack and stack[-1] < n:
            stack.pop()
            k -= 1
        stack.append(n)

    return ''.join(stack[:len(stack)-k])


if __name__ == '__main__':
    cases = [
        ('1924', 2),
        ('1231234', 3),
        ('4177252841', 4)
    ]

    for case in cases:
        output = solution(case[0], case[1])
        print(output)