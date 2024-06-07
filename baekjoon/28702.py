array = []
for _ in range(3):
    array.append(input().strip())

def check(i):
    if i % 3 == 0 and i % 5 == 0:
        return "FizzBuzz"
    elif i % 3 == 0 and i % 5 != 0:
        return "Fizz"
    elif i % 3 != 0 and i % 5 == 0:
        return "Buzz"
    else:
        return str(i)

i = 1
while True:
    if array[0] == check(i) and array[1] == check(i+1) and array[2] == check(i+2):
        print(check(i+3))
        exit()
    else:
        i += 1
    
