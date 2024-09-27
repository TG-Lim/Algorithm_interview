# Silver 2
import sys
input = sys.stdin.readline

def solve(N, prices):
    max_price = 0
    profit = 0
    for price in reversed(prices):
        if price > max_price:
            max_price = price
        else:
            profit += max_price - price
    return profit


if __name__ == '__main__':
    T = int(input())
    answers = []
    for _ in range(T):
        N = int(input())
        prices = list(map(int, input().split()))
        answer = solve(N, prices)
        answers.append(answer)
    for a in answers:
        print(a)
    exit()