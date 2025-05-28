import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    array = []

    for _ in range(N):
        x, a = map(int, input().strip().split())
        array.append((x, a))
    
    array.sort()
    
    total_people = sum([a[1] for a in array])
    
    accum = 0
    for x, a in array:
        accum += a
        if accum >= (total_people+1)//2:
            print(x)
            break


solution()