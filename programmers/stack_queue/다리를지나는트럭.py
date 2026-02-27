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