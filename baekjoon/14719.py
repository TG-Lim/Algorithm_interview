def solution():
    H, W = map(int, input().strip().split())
    array = list(map(int, input().strip().split()))

    if W < 3:
        print(0)
        exit()

    left = 0
    right = W-1
    lh = array[left]
    rh = array[right]
    answer = 0
    while left < right:
        if array[left] < array[right]: # 왼쪽이 더 작으므로 왼쪽이 이동
            left += 1
            lh = max(lh, array[left])
            answer += lh - array[left]

        else:
            right -= 1
            rh = max(rh, array[right])
            answer += rh - array[right]

    print(answer)
    exit()

solution()