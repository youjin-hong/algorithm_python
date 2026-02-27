import math
from collections import deque


def solution(progresses, speeds):
    queue = deque()
    result = []

    for i in range(len(progresses)):
        times = math.ceil((100 - progresses[i]) / speeds[i])
        queue.append(times)

    while queue:
        max_time = queue.popleft()
        count = 1

        while queue and queue[0] <= max_time:
            count += 1
            queue.popleft()

        result.append(count)

    return result