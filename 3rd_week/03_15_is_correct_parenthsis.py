def is_correct_parenthesis(string):
    stack = []

    for ch in string:
        if string[0] != '(' or string[-1] != ')': return False

        if ch == '(':
            stack.append(ch)
        else:
            if len(stack) != 0:
                stack.pop()

    return len(stack) == 0


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))