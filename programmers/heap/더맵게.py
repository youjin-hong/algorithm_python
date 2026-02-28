import heapq


def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) < 2: return -1

        first_scoville = heapq.heappop(scoville)
        second_scoville = heapq.heappop(scoville)

        new_scoville = first_scoville + 2 * second_scoville
        count += 1

        heapq.heappush(scoville, new_scoville)

    return count