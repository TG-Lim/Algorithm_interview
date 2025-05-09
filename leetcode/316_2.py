from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = Counter(s), set(), []
        # 알파벳 개수 집계, 본 것들, 스택
        for char in s:
            counter[char] -= 1 # 개수 빼기
            if char in seen:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0: # 스택이 있고, 사전순으로 뒤인 단어가 있고, 개수가 1개보다 많을 때
                seen.remove(stack.pop())
            
            stack.append(char)
            seen.add(char)

        return ''.join(stack)

if __name__ == '__main__':
    cases = [
        "bcabc",
        "cbacdcbc",
        "ebcabc"
    ]

    for case in cases:
        output = Solution().removeDuplicateLetters(case)
        print(output)