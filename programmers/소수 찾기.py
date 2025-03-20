def ethochae(n):
    if n < 2:
        return set()
    primes = [True]*(n+1)
    primes[0], primes[1] = False, False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]: # 소수면 배수인 것들 다 없애기
            for j in range(i*i, n+1, i):
                primes[j] = False

    return set([i for i in range(n+1) if primes[i]])

def back_tracking(lst, path, used, result, r):
    if len(path) == r:
        result.append(path[:])
        return

    for i in range(len(lst)):
        if not used[i]:
            used[i] = True
            path.append(lst[i])
            back_tracking(lst, path, used, result, r)
            path.pop()
            used[i] = False

def solution(numbers):
    answer = 0
    number_list = list(numbers)
    number_list.sort(reverse=True)
    largest_number = int(''.join(number_list))
    prime_numbers = ethochae(largest_number)
    is_checked = [False]*(largest_number+1)

    for r in range(1, len(number_list)+1):
        permutations = []
        back_tracking(number_list, [], [False]*len(number_list), permutations, r)

        for permutation in permutations:
            temp = int(''.join(permutation))
            if temp in prime_numbers and not is_checked[temp]:
                is_checked[temp] = True
                answer += 1

    return answer

if __name__ == '__main__':
    cases = ['17', '011']

    for case in cases:
        output = solution(case)
        print(output)
#