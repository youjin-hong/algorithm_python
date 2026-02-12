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


def get_linked_list_sum(linked_list_1, linked_list_2):
    result1 = ''
    result2 = ''
    cur1 = linked_list_1.head
    cur2 = linked_list_2.head

    while cur1 is not None:
        result1 += str(cur1.data)
        cur1 = cur1.next

    while cur2 is not None:
        result2 += str(cur2.data)
        cur2 = cur2.next

    return int(result1) + int(result2)


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))