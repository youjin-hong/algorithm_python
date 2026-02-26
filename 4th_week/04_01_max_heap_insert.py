# max Heap에 원소 추가하는 방법
# 1. 일단 맨 뒤에 넣어
# 2. 그 다음에 부모보다 큰지 비교해서 크면 부모랑 바꾸고, 아니면 계속 해

class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index != 1:
            # 1인 경우에는 root node라 더 비교할 게 없음. 올라갈 일이 없음
            # 2. 부모 노드랑 비교해서 내가 더 크다면 위치 바꾸지
            parent_index = cur_index // 2

            if self.items[cur_index] > self.items[parent_index]:
                self.items[cur_index], self.items[parent_index] = self.items[parent_index], self.items[cur_index]
                cur_index = parent_index
            else:
                break


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!