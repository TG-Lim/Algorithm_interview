N = int(input())
array = list(map(int, input().strip().split()))

array.sort()

min_left, min_right = None, None
min_property = int(2e9)

left, right = 0, N-1

while left < right:
    property = array[left] + array[right]
    
    if abs(property) < min_property:
        min_property = abs(property)
        min_left = array[left]
        min_right = array[right]
    
    if abs(array[left] + array[right-1]) < abs(property): # 오른쪽 옮기는 게 property 줄임
        right -= 1
    
    else:
        left += 1
        
print(min_left, min_right)