# Silver 4
import sys
N = int(input())
deck = list(map(int, sys.stdin.readline().strip().split()))
M = int(input())
cards = list(map(int, sys.stdin.readline().strip().split()))

counts = {}
for card in deck:
    if card in counts:
        counts[card] += 1
    else:
        counts[card] = 1

result = []
for i in range(len(cards)):
    if cards[i] not in counts:
        result.append(str(0))
    else:
        result.append(str(counts[cards[i]]))

print(' '.join(result))