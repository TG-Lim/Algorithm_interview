import sys
input = sys.stdin.readline

records = []
for _ in range(8):
    lap, team = input().strip().split()
    lap_list = lap.split(':')
    lap_time = int(lap_list[0])*60 + int(lap_list[1]) + int(lap_list[2])*0.001
    records.append((lap_time, team))

records.sort()

red = 0
blue = 0

score = {
    0: 10,
    1: 8,
    2: 6,
    3: 5,
    4: 4,
    5: 3,
    6: 2,
    7: 1
}

maximum_red = 10
maximum_blue = 10

for i, record in enumerate(records):
    if record[1] == 'B':
        blue += score[i]
        maximum_blue = min(maximum_blue, i)
    else:
        red += score[i]
        maximum_red = min(maximum_red, i)

if blue < red:
    print('Red')
elif blue > red:
    print('Blue')
else:
    if maximum_blue < maximum_red:
        print('Blue')
    else:
        print('Red')
exit()