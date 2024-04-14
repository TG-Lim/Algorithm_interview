N = int(input())
fact = 1

for i in range(1,N+1):
    fact *= i

fact = str(fact)[::-1]

index = 0
for i in range(len(fact)):
    if fact[i] != "0":
        index = i
        break

print(index)