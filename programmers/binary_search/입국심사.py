def solution(n, times):
    # 1. 탐색 범위 설정: 최소 1분부터 '가장 느린 사람 기준' 최대 시간까지
    min_minutes = 1
    max_minutes = max(times) * n
    result = max_minutes  # 정답을 담을 변수 (일단 최대로 설정)

    # 2. 이진 탐색 시작 (시간을 조절하며 최적의 지점을 찾음)
    while min_minutes <= max_minutes:
        # 이번 단계에서 검사해볼 '중간 시간' 계산
        mid_minutes = (min_minutes + max_minutes) // 2

        # 3. 'mid_minutes'라는 시간 동안 모든 심사관이 총 몇 명을 심사할 수 있는지 계산
        pass_people = 0
        for time in times:
            # 시간당 처리 가능한 인원수를 모두 더함 (예: 30분 // 7분 = 4명)
            pass_people += mid_minutes // time

        # 4. 비교 로직: n명보다 많이/똑같이 심사했는가?
        if pass_people >= n:
            # n명 이상 가능하면, 시간을 더 줄여볼 여지가 있음!
            result = mid_minutes  # 일단 현재 시간을 정답으로 기록
            max_minutes = mid_minutes - 1  # 더 짧은 시간 범위로 이동 (왼쪽 탐색)
        else:
            # n명을 다 못 받으면 시간이 부족한 것임!
            min_minutes = mid_minutes + 1  # 더 긴 시간 범위로 이동 (오른쪽 탐색)

    return result