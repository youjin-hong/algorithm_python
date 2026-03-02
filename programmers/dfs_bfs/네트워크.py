# 내 풀이
def solution(n, computers):
    # A -> B, B -> C일 때 A -> C (이행적 관계)
    # 우리는 네트워크 개수를 구해야 함
    # 얘는 그럼 깊이 우선 탐색?을 해야할까?

    visited = [False] * n
    count = 0

    def dfs(cur_index):
        visited[cur_index] = True
        for i in range(n):
            if computers[cur_index][i] == 1 and not visited[i]:
                dfs(i)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1

    return count


# stack을 이용한 풀이
