# Bronze 3
A, B = map(int, input().strip().split())
C = int(input())

hour = (B+C) // 60
B = (B+C) % 60
A = (A+hour) % 24
print(A,B)