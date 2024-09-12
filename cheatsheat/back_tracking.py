# Combination code implementation with Back-tracking

def combination(array, r):
    result = []

    def backtracking(start, comb): # 재귀 함수
        if len(comb) == r: # 원하는 조건 달성
            result.append(comb[:])
            return # 재귀함수 탈출 조건
        
        for i in range(start, len(array)):
            comb.append(array[i])
            backtracking(i+1, comb)
            comb.pop()
    
    backtracking(0, [])
    return result

def permuatation(array, r):
    result = []
    used = [False]*len(array)

    def backtrack(perm):
        if len(perm) == r:
            result.append(perm[:])
            return
        
        for i in range(len(array)):
            if not used[i]:
                perm.append(array[i])
                used[i] = True

                backtrack(perm)

                perm.pop()
                used[i] = False
    
    backtrack([])
    return result


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    print(combination(array, 3))
    print(permuatation(array, 2))