answer = []
while True:
    triangle = list(map(int, input().strip().split()))
    triangle.sort()

    if sum(triangle) == 0:
        break
    if sum(triangle[:2]) <= triangle[-1]:
        answer.append('Invalid')
    else:
        if len(set(triangle)) == 3:
            answer.append('Scalene')
        elif len(set(triangle)) == 2:
            answer.append('Isosceles')
        elif len(set(triangle)) == 1:
            answer.append('Equilateral')
    
print('\n'.join(answer))