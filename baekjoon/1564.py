N = int(input())
answer = 1 # 0!

for i in range(1, N+1):
    answer = (answer*i) # 10만으로 나눔. 5자리 수

print(answer)