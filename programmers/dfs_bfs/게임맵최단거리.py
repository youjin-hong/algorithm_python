from collections import deque


def solution(maps):
    ene_row = len(maps)
    ene_col = len(maps[0])

    # 상 하 좌 우
    direct_row = [0, 0, 1, -1]
    direct_col = [1, -1, 0, 0]

    queue = deque([(0, 0)])

    while queue:
        row, col = queue.popleft()

        for i in range(4):
            cur_row = row + direct_row[i]
            cur_col = col + direct_col[i]

            if 0 <= cur_row < ene_row and 0 <= cur_col < ene_col and maps[cur_row][cur_col] == 1:
                maps[cur_row][cur_col] = maps[row][col] + 1
                queue.append((cur_row, cur_col))

    result = maps[ene_row - 1][ene_col - 1]

    if result == 1:
        return -1
    return result



