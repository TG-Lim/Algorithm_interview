import sys

input = sys.stdin.readline

N, K = map(int, input().split())

meetings = []
for _ in range(N):
    a, b = map(int, input().strip().split())
    meetings.append((a, b))

rooms = [0]*K
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
if K == 1:
    for start, end in meetings:
        if start > rooms[0]:
            rooms[0] = end # 끝나는 시간 변경
            count += 1

else: # K >= 2
    for start, end in meetings:
        room_number = None
        diff = None
        for k in range(K):
            temp = start - rooms[k] 
            if temp > 0: # 시작시간이 더 뒤
                if room_number is None:
                    room_number = k
                    diff = temp
                else:
                    if diff > temp: # 가장 늦게 끝나는 것을 선택. 즉 다음 회의 시작 시간과 현재 회의 진행중인 시간 중 제일 나중에 끝나는 것 선택
                        diff = temp
                        room_number = k
            
        if room_number != None:
            rooms[room_number] = end
            count += 1

print(count)