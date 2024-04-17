# Bronze 3

d = int(input())
numbers = []
for _ in range(d):
    numbers.append(int(input()))

def make_number(n):
    transform = []
    while n >= 1:
        temp = n % 2
        transform.append(temp)
        n = n//2
    return transform

for n in numbers:
    result = make_number(n)
    answer = []
    for i in range(len(result)):
        if result[i] == 1:
            answer.append(str(i))
    print(' '.join(answer))