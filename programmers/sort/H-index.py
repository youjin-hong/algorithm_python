def solution(citations):
    # citations를 내림차순으로 정렬한다.
    citations.sort(reverse=True)

    # 현재 원소가 현재 확인 중인 논문 수보다 작아지는 지점이 오면, 기준점을 찾은 것이므로
    # return i
    for i in range(len(citations)):
        if citations[i] < i + 1:
            return i

    return len(citations)

