import sys

def check_balance(sentence):
    stack = []
    for s in sentence:
        if s == '(' or s == '[':
            stack.append(s)
        if s == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return 'no'
            else:
                stack.pop()
        if s == ']':
            if len(stack) == 0 or stack[-1] != '[':
                return 'no'
            else:
                stack.pop()
    if len(stack) == 0:
        return 'yes'
    else:
        return 'no'

sentences = []
while True:
    sentence = sys.stdin.readline().rstrip()
    if sentence == '.':
        break
    else:
        sentences.append(sentence)


for sentence in sentences:
    result = check_balance(sentence)
    print(result)