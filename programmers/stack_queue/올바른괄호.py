def solution(s):
    stack = []

    if s[0] != '(' or s[-1] != ')':
        return False

    for i in range(0, len(s)):

        if s[i] == '(':
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return False
            stack.pop()

    return len(stack) == 0

# 두 번째 내 풀이
def solution(s):
    if s[0] != '(' or s[-1] != ')': return False

    stack = []

    for ch in s:
        if len(stack) == 0 or ch == "(":
            stack.append(ch)
        else:
            stack.pop()

    return len(stack) == 0
