def cursordown(cursor: int, answer: list):
    cursor += 1
    answer.append('1')
    return cursor

def channelup(cursor: int, answer: list):
    if cursor > 0:
        array[cursor], array[cursor-1] = array[cursor-1], array[cursor]
        cursor -= 1
        answer.append('4')
        return cursor

N = int(input())
array = [input().strip() for _ in range(N)]
answer = []
cursor = 0
while True:
    if array[cursor] != 'KBS1': # KBS1로 이동
        cursor = cursordown(cursor, answer)
    else:
        cursor = channelup(cursor, answer)
    if array[0] == 'KBS1':
        break

while True:
    if array[cursor] != 'KBS2': # KBS2로 이동
        cursor = cursordown(cursor, answer)
    else:
        cursor = channelup(cursor, answer)
    if array[1] == 'KBS2':
        break

print(''.join(answer))
