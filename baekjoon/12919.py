# Gold 5

def can_transform(S, T):
    visited = set()

    def dfs(t):
        if t == S:
            return True
        if len(t) < len(S):
            return False
        if t in visited:
            return False
        visited.add(t)
        result = False
        if t[-1] == 'A':
            if dfs(t[:-1]):
                return True

        if t[0] == 'B':
            reversed_t = t[1:][::-1]
            if dfs(reversed_t):
                return True
        return False

    return dfs(T)

if __name__ == "__main__":
    S = input().strip()
    T = input().strip()

    print(1 if can_transform(S, T) else 0)