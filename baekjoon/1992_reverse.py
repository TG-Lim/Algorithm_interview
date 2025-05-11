def solution(quadtree, N):
    def decompress(idx, size):
        char = quadtree[idx]
        if char == '0' or char == '1':
            return [[char]*size for _ in range(size)], idx+1
        elif char == '(': # 추가 압축
            idx += 1
            half = size // 2

            a, idx = decompress(idx, half)
            b, idx = decompress(idx, half)
            c, idx = decompress(idx, half)
            d, idx = decompress(idx, half)

            top = [row_a + row_b for row_a, row_b in zip(a, b)]
            bottom = [row_c + row_d for row_c, row_d in zip(c, d)]
            return top + bottom, idx+1
    
    array, _ = decompress(0, N)
    return array


if __name__ == '__main__':
    answer = solution("((110(0101))(0010)1(0001))",8)
    for a in answer:
        print(''.join(a))
