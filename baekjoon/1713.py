import sys
input = sys.stdin.readline

N = int(input())
C = int(input())
recs = list(map(int, input().split()))

frames = []         # [student, count, time]
time = 0

for a in recs:
    time += 1
    # 1) 이미 게시된 학생인지 확인
    for f in frames:
        if f[0] == a:
            f[1] += 1
            break
    else:
        # 2) 새로 게시해야 할 때
        if len(frames) < N:
            frames.append([a, 1, time])
        else:
            # 3) 삭제할 후보 찾기
            frames.sort(key=lambda x: (x[1], x[2]))
            frames.pop(0)
            frames.append([a, 1, time])

# 최종 출력
result = sorted(f[0] for f in frames)
print(*result)
