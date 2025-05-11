N, X = map(int, input().strip().split())

length = [1]*(N+1)
patties = [1]*(N+1)

for i in range(1, N+1):
    length[i] = 2*length[i-1] +3
    patties[i] = 2*patties[i-1] +1

def count_patty(level, x):
    if level == 0:
        return 1 if x > 0 else 0
    
    if x == 1:
        return 0
    
    elif x <= 1 + length[level-1]: # 제일 앞에 번 빼고 판단
        return count_patty(level-1, x-1)
    
    elif x == 1 + length[level-1] + 1: # 레벨 N-1 에다가 패티 부분
        return patties[level-1] + 1
    
    elif x <= 1 + length[level-1] + 1 + length[level-1]: # 중간 이후 뒤에 레벨 N-1 부분
        return patties[level-1] + 1 + count_patty(level-1, x - (1 + length[level-1]+1))
    
    else:
        return patties[level]
    
print(count_patty(N, X))