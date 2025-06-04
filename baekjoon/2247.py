import sys
input_data = sys.stdin.readline
mod = int(1e6)
def sum_sigma_till(n: int) -> int:
    S = 0
    d = 1
    while d <= n:
        q = n // d
        last = n // q
        cnt = last - d + 1
        sum_d_to_last = (d + last) * cnt // 2
        S += q * sum_d_to_last
        d = last + 1
    return S % mod

def compute_CSOD(n: int) -> int:
    # 1) sum_{k=1}^n sigma(k)
    total_sigma = sum_sigma_till(n)
    # 2) CSOD(n) = total_sigma - n(n+1)/2 - n + 1
    return (total_sigma - (n * (n + 1) // 2) - n + 1) % mod

if __name__ == "__main__":
    n = int(input_data().strip())
    print(compute_CSOD(n))
