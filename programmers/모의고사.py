def generate_first(problem_num):
    return [ i % 5 + 1 for i in range(problem_num)]

def generate_second(problem_num):
    def make_num(i):
        if i % 2 == 0:
            return 2
        elif i % 8 == 1:
            return 1
        elif i % 8 == 3:
            return 3
        elif i % 8 == 5:
            return 4
        elif i % 8 == 7:
            return 5

    return [make_num(i) for i in range(problem_num)]

def generate_third(problem_num):
    mapping = {
        (0, 1): 3,
        (2, 3): 1,
        (4, 5): 2,
        (6, 7): 4,
        (8, 9): 5
    }

    def make_num2(j):
        index = j % 10
        for key in mapping:
            if index in key:
                return mapping[key]

    return [make_num2(j) for j in range(problem_num)]

def solution(answers):
    problem_num = len(answers)
    first = generate_first(problem_num)
    second = generate_second(problem_num)
    third = generate_third(problem_num)
    
    first_score = sum([1 for i in range(problem_num) if answers[i] == first[i]])
    second_score = sum([1 for i in range(problem_num) if answers[i] == second[i]])
    third_score = sum([1 for i in range(problem_num) if answers[i] == third[i]])
    
    scores = [first_score, second_score, third_score]
    max_score = max(scores)
    answer = [i + 1 for i in range(3) if scores[i] == max_score]

    return answer

if __name__ == "__main__":

    cases = [
        ([1, 2, 3, 4, 5], [1]),
        ([1, 3, 2, 4, 2], [1, 2, 3])
    ]

    for case in cases:
        output = solution(case[0])
        print(f"Output: {output} / Answer: {case[1]}")
