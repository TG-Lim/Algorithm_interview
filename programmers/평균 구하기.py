def solution(arr):
    return sum(arr)/len(arr)

if __name__ == '__main__':
    cases = [[1, 2, 3, 4], [5, 5]]
    for case in cases:
        answer = solution(case)
        print(answer)