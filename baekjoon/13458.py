# Bronze 2
import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0

for a in array:
    if a <= B: # 총 감독관 만으로 커버 가능
        b, c = 1, 0
    
    else:
        b = 1
        if (a-B) <= C: # 부감독관 한명만으로 커버 가능
            c = 1
        else:
            if (a-B) % C == 0:
                c = (a-B) // C
            else:
                c = ((a-B) // C) + 1
    

    answer += (b+c)

print(answer)