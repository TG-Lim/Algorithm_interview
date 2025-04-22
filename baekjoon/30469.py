import sys

def save_primes() -> list[bool]:
    """0~99 숫자에 대한 소수 여부 테이블 생성"""
    prime = [True] * 100
    prime[0] = prime[1] = False
    for i in range(2, 100):
        if prime[i]:
            for j in range(i * i, 100, i):
                prime[j] = False
    return prime

def check_prime(a: int, b: int, prime: list[bool]) -> bool:
    """두 자리 수 a*10 + b 가 소수인지 확인"""
    c = a * 10 + b
    return 10 <= c < 100 and prime[c]

def find_prime_sequence(a: int, b: int, n: int, prime: list[bool]) -> list[int] | None:
    """
    길이 n 짜리 숫자 시퀀스를 만들되,
    연속된 두 자리 수가 모두 소수이어야 함.
    실패 시 None 반환.
    """
    # 각 자리 저장할 리스트
    number = [0] * n
    # 시작 소수 a 의 십의 자리, 일의 자리로 분해
    number[0] = a // 10
    number[1] = a % 10

    # 중간 자리(2번째 인덱스부터 n-3번째 인덱스) 채우기
    for i in range(2, n - 2):
        found = False
        # 다음 일의 자리 d 를 1~9 중에서 찾아서 소수(이전 자리와) 만들기
        for d in range(1, 10):
            if check_prime(number[i - 1], d, prime):
                number[i] = d
                found = True
                break
        if not found:
            return None

    # 마지막 두 자리를 b 로 고정
    number[n - 2] = b // 10
    number[n - 1] = b % 10

    # 마지막 세 자리의 연결도 소수 조건 만족하는지 최종 확인
    if (check_prime(number[n - 3], number[n - 2], prime) and
        check_prime(number[n - 2], number[n - 1], prime)):
        return number
    else:
        return None

def main():
    prime = save_primes()

    # 입력
    a, b, n = map(int, sys.stdin.readline().split())

    # a, b 가 10~99 사이의 소수인지 먼저 검사
    if not (10 <= a < 100 and 10 <= b < 100 and prime[a] and prime[b]):
        print(-1)
        return

    seq = find_prime_sequence(a, b, n, prime)
    if seq is None:
        print(-1)
    else:
        # 각 자리 숫자를 문자열로 합쳐서 출력
        print(''.join(map(str, seq)))

if __name__ == "__main__":
    main()
