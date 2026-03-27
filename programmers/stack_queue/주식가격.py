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

# 세 번째 풀이(큐 활용 o)
from collections import deque


def solution(prices):
    queue = deque(prices)
    result = []

    while queue:
        curr_price = queue.popleft()
        seconds = 0

        for next_price in queue:
            seconds += 1

            if next_price < curr_price:
                break

        result.append(seconds)
    return result
