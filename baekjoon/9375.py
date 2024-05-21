# Silver 3
T = int(input())

def solution():
    n = int(input())
    closet = {}
    for _ in range(n):
        _, type = input().strip().split()
        if type not in closet:
            closet[type] = 1
        else:
            closet[type] += 1
            
    answer = 1
    for count in closet.values():
        answer *= (count + 1)
        
    return answer - 1
    
answers = []
for _ in range(T):
    answers.append(solution())
print('\n'.join(str(a) for a in answers))