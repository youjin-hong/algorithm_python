def solution(n, lost, reserve):
    result = [1] * n

    for num in lost:
        result[num - 1] -= 1

    for num in reserve:
        result[num - 1] += 1

    for i in range(len(result)):
        if result[i] == 0:
            if i > 0 and result[i - 1] == 2:
                result[i - 1] -= 1
                result[i] += 1
            elif i < len(result) - 1 and result[i + 1] == 2:
                result[i + 1] -= 1
                result[i] += 1

    while 0 in result:
        result.remove(0)

    return len(result)
