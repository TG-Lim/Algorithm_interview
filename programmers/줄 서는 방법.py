from math import factorial
def solution(n, k):
    used = [False]*(n+1)
    answer = []
    product = factorial(n-1)

    while len(answer) < n:
        available = [i for i in range(1, n+1) if not used[i]]
        if len(available) == 1:
            answer += available
            break

        for i in range(len(available)):
            if i * product < k <= (i+1)*product:
                answer.append(available[i])
                used[available[i]] = True
                k -= i*product
                product //= len(available) - 1
                break
    
    return answer
    

if __name__ == '__main__':
    print(solution(3, 5)) # [3, 1, 2]
    print(solution(1, 1)) # [1]
    print(solution(2, 1)) # [1, 2]