from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = Counter(s), set([]), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue

            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)

if __name__ == '__main__':
    cases = [
        "bcabc",
        "cbacdcbc"
    ]

    for case in cases:
        output = Solution().removeDuplicateLetters(case)
        print(output)
