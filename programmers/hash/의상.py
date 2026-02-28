def solution(clothes):
    dict = {}
    count = 1

    for cloth, sort in clothes:
        if sort in dict:
            dict[sort] += 1
        else:
            dict[sort] = 1

    for value in dict.values():
        count *= (value + 1)
        # 옷이 A, B 있으면
        # 1) A를 입는다.
        # 2) B를 입는다.
        # 3) 아무것도 입지 않는다.

    return count - 1