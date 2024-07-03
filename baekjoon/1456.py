# Gold 5

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]

def count_power_primes(A, B):
    P = int(B ** 0.5)
    primes = sieve_of_eratosthenes(P)
    answer = 0

    for p in primes:
        number = p * p
        while number <= B:
            if number >= A:
                answer += 1
            if number > B // p:
                break
            number *= p

    return answer

A, B = map(int, input().split())
print(count_power_primes(A, B))