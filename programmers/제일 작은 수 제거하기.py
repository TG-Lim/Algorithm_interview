def solution(arr):
    min_value = min(arr)
    min_index = arr.index(min_value)
    arr.pop(min_index)
    if not arr:
        return [-1]
    else:
        return arr

if __name__ == '__main__':
    cases = [[4, 3, 2, 1], [10]]
    for case in cases:
        output = solution(case)
        print(output)