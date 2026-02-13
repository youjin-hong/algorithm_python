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

    # 정답 - 근데 여기서 더 개선할 수 있음
    def get_kth_node_from_last_before(self, k):
        length = 1  # head는 노드 길이가 1이므로 1부터 시작
        cur = self.head

        while cur.next is not None:
            cur = cur.next
            length += 1
        print('length is ', length) # 이러면 linked list의 현재 길이를 알 수 있음

        end_length = length - k
        cur = self.head

        for i in range(end_length):
            cur = cur.next
        return cur

    # 개선한 버전
    def get_kth_node_from_last(self, k):
        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        return slow


    # 내 풀이 - 틀린 풀이
    def get_kth_node_from_last_mine(self, k):
        cur = self.head
        step = 0

        while step < k:
            cur = cur.next
            step += 1

        return cur


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!