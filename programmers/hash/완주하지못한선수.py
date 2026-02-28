# 내 풀이
def solution(participant, completion):
    dict = {}

    for name in participant:
        if name in dict:
            dict[name] += 1
        else:
            dict[name] = 1

    for name in completion:
        if name in dict:
            dict[name] -= 1

    for k, v in dict.items():
        if v != 0:
            return k


# 효율적인 풀이
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


# 해시를 이용한 정석 풀이
def solution(participant, completion):
    answer = 0
    hash_dict = {}

    # 1. 모든 참가자의 해시값을 더함
    for person in participant:
        h = hash(person)
        answer += h
        hash_dict[h] = person  # 해시값에 해당하는 이름을 저장

    # 2. 모든 완주자의 해시값을 뺌
    for person in completion:
        answer -= hash(person)

    # 3. 남은 해시값이 바로 완주하지 못한 사람의 해시값!
    return hash_dict[answer]