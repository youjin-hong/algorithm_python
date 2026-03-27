from collections import deque


def solution(bridge_length, weight, truck_weights):
    current_weight = 0
    passing = deque([0] * bridge_length)
    pending = deque(truck_weights)
    time = 0

    while passing:
        time += 1
        curr_truck = passing.popleft()
        current_weight -= curr_truck

        if pending:
            if pending[0] + current_weight <= weight:
                new_truck = pending.popleft()
                passing.append(new_truck)
                current_weight += new_truck
            else:
                passing.append(0)

    return time

# 두 번째 내 풀이
from collections import deque


def solution(bridge_length, weight, truck_weights):
    times = 0
    pending = deque(truck_weights)
    crossing = deque([0] * bridge_length)
    bridge_weight = 0

    for truck in crossing:
        bridge_weight += truck

    while crossing:
        times += 1
        out = crossing.popleft()
        bridge_weight -= out

        if pending:
            if bridge_weight + pending[0] <= weight:
                curr_truck = pending.popleft()
                crossing.append(curr_truck)
                bridge_weight += curr_truck
            else:
                crossing.append(0)

    return times
