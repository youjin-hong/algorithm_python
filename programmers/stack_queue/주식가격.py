def solution(prices):
    stack = []
    n = len(prices)

    for i in range(n):
        time = 0
        for j in range(i + 1, n):
            time += 1
            if prices[j] < prices[i]:
                time = j - i
                break
        stack.append(time)

    return stack

# 두 번째 풀이(스택 활용 x)
def solution(prices):
    result = []

    for i in range(len(prices)):
        seconds = 0
        for j in range(i + 1, len(prices)):
            seconds += 1
            if prices[i] > prices[j]:
                break
        result.append(seconds)

    return result

