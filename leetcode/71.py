class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        path = [p for p in path if p != '']
        for p in path:
            if p == '..': # 위 경로로 올라가는 거 이므로 꺼냐야 함
                if stack:
                    stack.pop()
                continue
            elif p == '.': # 현재 경로이므로 그냥 생략
                continue
            stack.append(p)
        result = [''] # 제일 처음에는 / 로 시작
        result.extend(stack)

        if result == ['']:
            return '/'
        return '/'.join(result)
    
if __name__ == '__main__':
    cases = [
        "/home/",
        "/home//foo/",
        "/home/user/Documents/../Pictures",
        "/../",
        "/.../a/../b/c/../d/./",
    ]

    for case in cases:
        output = Solution().simplifyPath(case)
        print(output)