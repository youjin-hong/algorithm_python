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

# 두 번째 내 풀이
import math


def solution(progresses, speeds):
    launch_days = []

    for i in range(len(progresses)):
        complete_progress = math.ceil((100 - progresses[i]) / speeds[i])
        launch_days.append(complete_progress)

    result = []
    count = 1
    max_day = launch_days[0]
    for i in range(1, len(launch_days)):

        if max_day >= launch_days[i]:
            count += 1
        else:
            max_day = launch_days[i]
            result.append(count)
            count = 1
    result.append(count)

    return result