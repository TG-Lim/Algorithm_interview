# Gold 5
import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

A_cards = list(set((map(int, input().split()))))
B_cards = list(set((map(int, input().split()))))
C_cards = list(set((map(int, input().split()))))

def is_valid(diff, A_cards, B_cards, C_cards):
    i, j, k = 0, 0, 0
    while i < len(A_cards) and j < len(B_cards) and k < len(C_cards):
        a, b, c = A_cards[i], B_cards[j], C_cards[k]
        current_max = max(a, b, c)
        current_min = min(a, b, c)
        
        if current_max - current_min <= diff:
            return True
        
        # 최솟값을 가진 포인터를 다음으로 이동
        if current_min == a:
            i += 1
        elif current_min == b:
            j += 1
        else:
            k += 1
    
    return False

def minimum_penalty_binary_search(A_cards, B_cards, C_cards):
    A_cards.sort()
    B_cards.sort()
    C_cards.sort()
    
    low, high = 0, max(max(A_cards) - min(A_cards), max(B_cards) - min(B_cards), max(C_cards) - min(C_cards))
    result = high

    while low <= high:
        mid = (low + high) // 2
        if is_valid(mid, A_cards, B_cards, C_cards):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result

result = minimum_penalty_binary_search(A_cards, B_cards, C_cards)
print(result)