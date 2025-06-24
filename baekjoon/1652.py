string = input().strip()

if string.isdigit():
    print(len(string))
    exit()

string_list = list(string)

left_indices = []
braket_pair = {}

for i in range(len(string_list)):
    if string_list[i] == '(':
        left_indices.append(i)
    elif string_list[i] == ')':
        last_index = left_indices.pop()
        braket_pair[last_index] = i
    else:
        continue

def decompress(start, end):
    total_length = 0
    i = start
    
    while i < end:
        if string[i].isdigit():
            if i + 1 < end and string[i+1] == '(': # 압축된 경우
                k = int(string[i])
                j = braket_pair[i+1]
                inner_length = decompress(i+2, j)
                total_length += k*inner_length
                i = j + 1
            else:
                total_length += 1
                i += 1
        elif string[i] == '(':
            i += 1
        elif string[i] == ')':
            i += 1

    return total_length
print(decompress(0, len(string)))