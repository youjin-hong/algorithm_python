from collections import deque


def can_change(curr_word, word):
    correct_count = 0

    for i in range(len(curr_word)):
        if curr_word[i] == word[i]:
            correct_count += 1

    if correct_count >= len(curr_word) - 1:
        return True
    else:
        return False


def solution(begin, target, words):
    # begin에서 target으로 변환하는 가장 짧은 변환 단계 구하기 => 최소값이므로 bfs 이용
    if target not in words:
        return 0

    visited = [False] * len(words)
    queue = deque([(begin, 0)])  # (현재 단어, 변환 횟수)

    while queue:
        curr_word, change_count = queue.popleft()

        if curr_word == target:
            return change_count

        for i in range(len(words)):
            if can_change(curr_word, words[i]) and not visited[i]:
                visited[i] = True
                queue.append((words[i], change_count + 1))

    return visited



