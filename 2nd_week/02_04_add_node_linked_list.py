class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):
        new_node = Node(value)

        # index가 0이 된다면 어떻게 될까?를 항상 고민해야 한다
        if index == 0:
            new_node.next = self.head  # 먼저 기존 헤드를 바라보게 만들어야 함
            self.head = new_node  # 새로운 헤드로 임명됨
            return # 이걸 안 쓰면 아래 코드들이 실행돼서 꼬임.

        # get_node 함수를 이용하면 된다
        prev_node = self.get_node(index-1)
        next_node = prev_node.next

        prev_node.next = new_node
        new_node.next = next_node



linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(0, 3)
linked_list.print_all()