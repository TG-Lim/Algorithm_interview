class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        total_count = {}
        for alphabet in s:
            if alphabet in total_count:
                total_count[alphabet] += 1
            else:
                total_count[alphabet] = 1

        partitions = []
        temp = set()
        cnt = 0
        for alphabet in s:
            if alphabet not in temp:
                temp.add(alphabet)
            total_count[alphabet] -= 1
            if total_count[alphabet] == 0:
                temp.remove(alphabet)
            cnt += 1

            if not temp:
                partitions.append(cnt)
                cnt = 0

        return partitions


if __name__ == '__main__':
    cases = [
        "ababcbacadefegdehijhklij",
        "eccbbbbdec"
    ]

    for case in cases:
        output = Solution().partitionLabels(case)
        print(output)