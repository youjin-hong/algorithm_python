# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!

# dfs의 본질은 "끝까지 찾아간다"이다.
# 끝까지 찾아갔다가 "없어?? 돌아와 돌아와 돌아 나와" "다른 선택지 가보자" 반복
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}

# 1. 시작 노드를 스택에 넣는다.
# 2. 현재 스택의 노드를 빼서 visited에 추가한다.
# 3. 현재 방문한 노드의 인접한 노드 중 방문하지 않은 노드를 스택에 추가한다.
# 위의 과정을 스택이 빌 때까지 반복한다.
def dfs_stack(adjacent_graph, start_node):
    stack = [start_node]
    visited = []

    while stack:
        cur_node = stack.pop()
        visited.append(cur_node)

        for adjacent_node in adjacent_graph[cur_node]:
            if adjacent_node not in visited:
                stack.append(adjacent_node)

    return visited


print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!