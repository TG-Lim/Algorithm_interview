N, M = map(int, input().strip().split()) 
array = list(map(int, input().strip().split()))

happy = sum([a+1 for a in array])

delta = M - happy # 우울할 날
if delta <= 0:
    print(0)
    exit()
    
length = N + 1 # N+1 구간에 우울할 날 할당가능
mok, namerji = delta // length, delta % length

cnt = {
    mok+1: namerji,
    mok: length - namerji
}

answer = 0
for key, value in cnt.items():
    if key == 0:
        continue
    else:
        answer += (key*(key+1)*(2*key+1)/6)*value
print(int(answer))