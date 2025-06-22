from collections import deque

A, B, C = map(int, input().strip().split())

visited = set()
answers = set()

queue = deque()
queue.append((0, 0, C))  # 초기 상태: A=0, B=0, C=C

def pour(x, y, limit):
    """x에서 y로 물을 붓는다. y는 limit까지 가능"""
    return min(x, limit - y)

while queue:
    a, b, c = queue.popleft()

    if (a, b, c) in visited:
        continue
    visited.add((a, b, c))

    if a == 0:
        answers.add(c)

    # A → B
    d = pour(a, b, B)
    queue.append((a - d, b + d, c))

    # A → C
    d = pour(a, c, C)
    queue.append((a - d, b, c + d))

    # B → A
    d = pour(b, a, A)
    queue.append((a + d, b - d, c))

    # B → C
    d = pour(b, c, C)
    queue.append((a, b - d, c + d))

    # C → A
    d = pour(c, a, A)
    queue.append((a + d, b, c - d))

    # C → B
    d = pour(c, b, B)
    queue.append((a, b + d, c - d))

print(" ".join(map(str, sorted(answers))))