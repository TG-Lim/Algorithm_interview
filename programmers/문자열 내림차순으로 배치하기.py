def solution(s):
    string_list = [(ord(string), string) for string in s]
    string_list.sort(reverse=True)
    string_list = [string[1] for string in string_list]
    answer = ''.join(string_list)
    return answer


print(solution("Zbcdefg"))