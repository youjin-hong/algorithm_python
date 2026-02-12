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

def get_single_linked_list_sum(linked_list):
    sum = 0
    cur = linked_list.head

    while cur is not None:
        sum = sum * 10 + cur.data
        cur = cur.next

    return sum


def get_linked_list_sum(linked_list_1, linked_list_2):
     # 중복되는 코드는 불편해야 한다
     # get_single_linked_list_sum 함수로 추출해 중복을 제거해보자
     return get_single_linked_list_sum(linked_list_1) + get_single_linked_list_sum(linked_list_2)



linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))