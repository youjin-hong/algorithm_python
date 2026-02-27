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
