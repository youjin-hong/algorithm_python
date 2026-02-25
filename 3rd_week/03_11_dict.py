
# put(key, value): dictionary에 key 해당하는 곳에 value를 저장해두겠다.
# get(key): dictionary에 key 해당하는 value를 반환해라

class Dict:
    def __init__(self):
        self.items = [None]*8

        # 1. Chaining 기법: 충돌이 발생했을 때, 그 값들을 Linked List로 관리한다.
        # 

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index] = value

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]

my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))