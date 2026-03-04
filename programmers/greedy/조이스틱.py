# def solution(name):
#     count = 0

#     for ch in name:
#         up = ord(ch) - ord('A')
#         down = ord('Z') - ord(ch) + 1

#         count += min(up, down)

#     count += (len(name)-1)
#     return count


def solution(name):
    # 1. 알파벳 변경 횟수 계산
    spell_count = 0
    for ch in name:
        spell_count += min(ord(ch) - ord('A'), ord('Z') - ord(ch) + 1)

    # 2. 커서 이동 횟수 계산 (최솟값 찾기)
    n = len(name)
    move = n - 1  # 기본값: 오른쪽으로 쭉 가기

    for i in range(n):
        # 다음 글자부터 연속된 'A'가 어디까지인지 찾기
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            next_i += 1

        # i: 현재 위치, next_i: 'A' 뭉치가 끝난 뒤의 다음 글자 위치
        # min(기존 이동, 오른쪽 갔다 왼쪽 꺾기, 왼쪽 먼저 갔다 오른쪽 꺾기)
        move = min(move, i * 2 + (n - next_i), (n - next_i) * 2 + i)

    return spell_count + move