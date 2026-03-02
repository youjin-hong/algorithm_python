# 내 풀이
def solution(numbers, target):
    cur_index = 0
    cur_sum = 0
    n = len(numbers)
    answer = []
    count = 0

    def dfs_recursion(cur_index, cur_sum):
        if cur_index == n:
            answer.append(cur_sum)
            return

        minus = dfs_recursion(cur_index + 1, cur_sum - numbers[cur_index])
        plus = dfs_recursion(cur_index + 1, cur_sum + numbers[cur_index])

    dfs_recursion(0, 0)

    for num in answer:
        if num == target:
            count += 1

    return count

# stack을 이용한 풀이
def solution(numbers, target):
    n = len(numbers)
    count = 0
    # 스택에 (현재 인덱스, 현재까지의 합)을 담습니다.
    # 초기값: 0번 인덱스부터 시작, 합계는 0
    stack = [(0, 0)]

    while stack:
        cur_index, cur_sum = stack.pop()  # 파이썬의 언패킹 방식으로 자바스크립트의 "구조분해할당"이라고 생각하면 됨

        # 모든 숫자를 다 사용했을 때
        if cur_index == n:
            if cur_sum == target:
                count += 1
            continue  # 다음 스택 요소를 확인하러 갑니다.

        # 다음 숫자를 처리하기 위해 두 갈래 길을 스택에 넣습니다.
        # (다음 인덱스, 현재 합 + 다음 숫자)
        # (다음 인덱스, 현재 합 - 다음 숫자)
        stack.append((cur_index + 1, cur_sum + numbers[cur_index]))
        stack.append((cur_index + 1, cur_sum - numbers[cur_index]))

    return count