
class Node:
    def __init__(self, data):
        self.data = data
        # head는 다음 칸을 지정해주지 않고 ["시멘트"] 이런 식으로
        # 각각의 화물칸만 만들어 놓을 예정이므로 None으로 지정
        self.next = None

# node = Node(5)
# print(node.data, node.next)
#
# next_node = Node(3)
# node.next = next_node

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    # LinkedList의 가장 끝에 있는 노드에 새로운 노드를 연결해줘라는 행동을
    # 이 클래스에게 하게 만들자
    def append(self, value):
        cur = self.head

        while cur.next is not None:
            cur = cur.next

        cur.next = Node(value)

    # linked_list에서 저장한 head를 따라가면서 현재 있는 노드들을 전부 출력해주는 함수
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
linked_list.print_all()

# 현재 상태 (맨 뒤에 9를 넣어주려면 head부터 끝까지 이동해야 하는데, 이 때 맨 뒤의 node는 next가 없다는 점을 이용하자!!)
# head
# [5] -> [3] -> [7] -> [6] -> [8] -> None
# cur = head
# cur = cur.next


# 원하는 상태 상태
# head                               new
# [5] -> [3] -> [7] -> [6] -> [8] -> [9]

