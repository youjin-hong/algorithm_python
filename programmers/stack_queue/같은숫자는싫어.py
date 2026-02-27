def solution(arr):
    stack = []

    for num in arr:
        if len(stack) == 0 or stack[-1] != num:
            stack.append(num)

    return stack


