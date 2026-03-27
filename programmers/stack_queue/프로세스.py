from collections import deque


def solution(priorities, location):
    queue = deque()

    for i in range(len(priorities)):
        queue.append([priorities[i], i])

    result = 0

    while queue:
        cur_process = queue.popleft()
        is_first = True

        for item in queue:
            if item[0] > cur_process[0]:
                is_first = False
                break

        if is_first == False:
            queue.append(cur_process)
        else:
            result += 1
            if cur_process[1] == location:
                return result


# 두 번째 풀이
from collections import deque


def solution(priorities, location):
    queue = deque((chr(pri + 65), i) for i, pri in enumerate(priorities))
    count = 0

    while queue:
        curr_item = queue.popleft()

        if any(curr_item[0] < item[0] for item in queue):
            queue.append(curr_item)
        else:
            count += 1

            if curr_item[1] == location:
                return count



