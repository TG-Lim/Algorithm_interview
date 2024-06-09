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

for i in range(3):
    if array[i].isdigit():
        temp = int(array[i]) + 3-i
        break

print(check(temp))