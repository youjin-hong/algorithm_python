def solution(phone_book):
    n = len(phone_book)
    phone_book.sort()

    for i in range(n - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    return True

# 해시를 이용한 풀이
def solution(phone_book):
    # 1. 모든 전화번호를 해시 맵(딕셔너리)에 담습니다. 📥
    hash_map = {}
    for number in phone_book:
        hash_map[number] = True

    # 2. 각 전화번호의 접두어가 해시 맵에 있는지 확인합니다. 🔍
    for number in phone_book:
        prefix = ""
        for digit in number:
            prefix += digit
            # 현재까지 만든 접두어가 해시 맵에 있고, 본인이 아니라면?
            if prefix in hash_map and prefix != number:
                return False

    return True