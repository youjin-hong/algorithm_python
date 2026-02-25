
# put(key, value): dictionary에 key 해당하는 곳에 value를 저장해두겠다.
# get(key): dictionary에 key 해당하는 value를 반환해라

class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))  # eg. ["333", 7] -> ["77", 6]

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v
linked_tuple = LinkedTuple()
linked_tuple.add("333", 7)


# 같은 인덱스로 접근했을 떄 "충돌"이 발생하는 건 해시(dict)의 어쩔 수 없는 문제점임. 해결 방안으로는 아래와 같음
# 1. Chaining 기법: 충돌이 발생했을 때, 그 값들을 Linked List로 관리한다.
class LinkedDict:
    def __init__(self):
        self.items = []

        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value) # index 번째의 LinkedTuple에 [(key, value)] 추가해줌
                                          # 한 번 더 호출되면?
                                          # index 번째의 LinkedTuple [(key, value), (key2, value2)]

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)  # LinkedTuple임.

my_dict = LinkedDict()
my_dict.put("test", 3)
print(my_dict.get("test"))