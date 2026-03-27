def solution(arr):
    stack = []

    for num in arr:
        if len(stack) == 0 or stack[-1] != num:
            stack.append(num)

    return stack


# 두 번째 내 풀이 (시간 복잡도 O(N)
def solution(arr):
    result = []

    for i in range(len(arr)):
        if i == 0 or arr[i] != result[-1]:
            result.append(arr[i])

    return result